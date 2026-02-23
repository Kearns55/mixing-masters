from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Course, Level, Purchase, SupplyItem
from .forms import CourseForm
import stripe

# Create your views here.


class CourseList(ListView):
    model = Course
    template_name = "courses/course_list.html"
    context_object_name = "courses"


class CourseDetail(DetailView):
    model = Course
    template_name = "courses/course_detail.html"
    context_object_name = "course"


def homepage(request):
    courses = Course.objects.all()
    return render(request, "home/index.html", {"courses": courses})


def create_checkout_session(request, pk):
    course = Course.objects.get(pk=pk)

    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price_data': {
                'currency': 'usd',
                'product_data': {
                    'name': course.name,
                    'description': course.description,
                },
                'unit_amount': course.price * 100,  # Stripe uses cents
            },
            'quantity': 1,
        }],
        mode='payment',
        success_url=request.build_absolute_uri(reverse('courses:payment_success')),
        cancel_url=request.build_absolute_uri(reverse('courses:payment_cancel')),
    )
    # Save the purchase record with the Stripe payment ID
    Purchase.objects.create(
        user=request.user,
        course=course,
        stripe_payment_id=session.id
    )
    return redirect(session.url, code=303)


def payment_success(request):
    return render(request, 'courses/success.html')


def payment_cancel(request):
    return render(request, 'courses/cancel.html')


@login_required
def my_courses(request):
    # Get all purchases for the logged-in user
    purchases = Purchase.objects.filter(user=request.user)
    courses = [purchase.course for purchase in purchases]
    return render(request, 'courses/my_courses.html', {'courses': courses})


@login_required
def create_course(request):
    if not request.user.is_superuser:
        messages.error(request, "You do not have permission to create courses.")
        return redirect('courses:course_list')
    if request.method == 'POST':
        # If "+ Add Supply" clicked
        if 'add_supply' in request.POST:
            name = request.POST.get('new_supply_name')
            supply, created = SupplyItem.objects.get_or_create(name=name)
            if created:
                messages.success(request, "Supply item added successfully.")
            else:
                messages.info(request, "Supply item already exists.")
            form = CourseForm()  # reload form so new supply appears
            return render(request, 'courses/create_course.html', {'form': form})
        # Add level
        if 'add_level' in request.POST:
            name = request.POST.get('new_level_name')
            level, created = Level.objects.get_or_create(name=name)
            if created:
                messages.success(request, "Level added successfully.")
            else:
                messages.info(request, "Level already exists.")
            
            form = CourseForm()  # reload form so new level appears
            return render(request, 'courses/create_course.html', {'form': form})
        
        form = CourseForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Course created successfully.")
            return redirect('courses:course_list')
        messages.error(request, "There was an error creating the course. Please check the form and try again.")
    else:
        form = CourseForm()
    return render(request, 'courses/create_course.html', {'form': form})


@login_required
def update_course(request, pk):
    if not request.user.is_superuser:
        messages.error(request, "You do not have permission to update courses.")
        return redirect('courses:course_list')
    course = get_object_or_404(Course, pk=pk)
    form = CourseForm(request.POST, request.FILES, instance=course)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, "Course updated successfully.")
            return redirect('courses:course_list')
        messages.error(request, "There was an error updating the course. Please check the form and try again.")
    return render(request, 'courses/update_course.html', {'form': form, 'course': course})


@login_required
def delete_course(request, pk):
    if not request.user.is_superuser:
        messages.error(request, "You do not have permission to delete courses.")
        return redirect('courses:course_list')
    course = get_object_or_404(Course, pk=pk)
    if request.method == 'POST':
        course.delete()
        messages.success(request, "Course deleted successfully.")
        return redirect('courses:course_list')
    return render(request, 'courses/delete_course.html', {'course': course})

