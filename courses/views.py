from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
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


def create_checkout_session(request, pk):
    course = Course.objects.get(pk=pk)

    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        customer_email=request.user.email,
        line_items=[{
            'price_data': {
                'currency': 'eur',
                'product_data': {
                    'name': course.name,
                    'description': course.description,
                },
                'unit_amount': course.price * 100,  # Stripe uses cents
            },
            'quantity': 1,
        }],
        mode='payment',
        success_url=request.build_absolute_uri(
            reverse('courses:payment_success')
        ) + "?session_id={CHECKOUT_SESSION_ID}",  # ← important
        cancel_url=request.build_absolute_uri(
            reverse('courses:payment_cancel')
        ),
        metadata={
            'user_id': request.user.id,
            'course_id': course.id
        }
    )
    return redirect(session.url, code=303)


@login_required
def payment_success(request):
    session_id = request.GET.get("session_id")

    if not session_id:
        messages.error(request, "No session ID provided.")
        return redirect("courses:course_list")

    session = stripe.checkout.Session.retrieve(session_id)

    if session.payment_status != "paid":
        messages.error(request, "Payment not completed.")
        return redirect("courses:course_list")

    user_id = session.metadata.get("user_id")
    course_id = session.metadata.get("course_id")

    if str(request.user.id) != user_id:
        messages.error(request, "Unauthorized access.")
        return redirect("courses:course_list")

    course = Course.objects.get(id=course_id)

    # Prevent duplicate purchases
    purchase, created = Purchase.objects.get_or_create(
        user=request.user,
        course=course,
        stripe_payment_id=session.id
    )

    if created:
        send_purchase_email(request.user, course)

    return render(request, "courses/success.html", {"course": course})


def send_purchase_email(user, course):
    send_mail(
        subject="Your Course is Ready 🎉",
        message=f"""
        Hi {user.username},

        Thank you for purchasing {course.name}.

        You can now view your workshop details in your dashboard.

        All the best,
        Mixing Masters
        """,
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[user.email],
        fail_silently=False,
    )


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

    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES, instance=course)
        if form.is_valid():
            form.save()
            messages.success(request, "Course updated successfully.")
            return redirect('courses:course_list')
        else:
            messages.error(request, "There was an error updating the course. Please check the form and try again.")
    else:
        # 🔥 This is what auto-populates the form
        form = CourseForm(instance=course)

    return render(request, 'courses/update_course.html', {
        'form': form,
        'course': course
    })

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