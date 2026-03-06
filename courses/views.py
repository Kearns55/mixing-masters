from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.db import IntegrityError
from .models import Course, Level, Purchase, SupplyItem
from .forms import CourseForm, LevelForm, SupplyItemForm
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


@login_required
def create_checkout_session(request, pk):
    course = get_object_or_404(Course, pk=pk)

    # Blocks stripe payment if user already purchased
    if Purchase.objects.filter(user=request.user, course=course).exists():
        messages.warning(request, "You have already purchased this workshop.")
        return redirect("courses:my_courses")  # Redirect to their purchased workshops

    # Only create Stripe session if not purchased
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
                'unit_amount': int(course.price * 100),
            },
            'quantity': 1,
        }],
        mode='payment',
        success_url=request.build_absolute_uri(
            reverse('courses:payment_success')
        ) + "?session_id={CHECKOUT_SESSION_ID}",
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
    try:
        Purchase.objects.create(
            user=request.user,
            course=course,
            stripe_payment_id=session.id
        )
        send_purchase_email(request.user, course)

    except IntegrityError:
        messages.info(request,
                      "You have already purchased this workshop.")
        return redirect("courses:course_list")

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


def _add_level_and_select(request, data):
    """Helper function to add new levels and pre-select on form creation."""
    name = (request.POST.get("new_level_name") or "").strip()
    if not name:
        messages.error(request, "Please enter a level name.")
        return None

    level, created = Level.objects.get_or_create(name=name)
    messages.success(
        request,
        "Level added successfully." if created else "Level already exists."
    )

    # Auto-select the new/existing level
    data["level"] = str(level.id)
    return level


def _add_supply_and_select(request, data):
    """Helper function to add new supply and pre-select on form creation."""
    name = (request.POST.get("new_supply_name") or "").strip()
    if not name:
        messages.error(request, "Please enter a supply name.")
        return None

    supply, created = SupplyItem.objects.get_or_create(name=name)
    messages.success(
        request,
        "Supply item added successfully." if created else "Supply item already exists."
    )

    # Auto-select: add to the selected supplies list
    selected = data.getlist("supplies")  # e.g. ["1", "3"]
    supply_id = str(supply.id)
    if supply_id not in selected:
        selected.append(supply_id)
        data.setlist("supplies", selected)

    return supply


@login_required
def create_course(request):
    if not request.user.is_superuser:
        messages.error(request, "You do not have permission to create courses.")
        return redirect('courses:course_list')
    if request.method == 'POST':
        # Make a mutable copy of POST data to modify for adding levels/supplies
        data = request.POST.copy()

        # If "+ Add Supply" clicked
        if 'add_supply' in request.POST:
            _add_supply_and_select(request, data)
            form = CourseForm(data, request.FILES)
            return render(request, 'courses/create_course.html', {'form': form})
        # Add level
        if 'add_level' in request.POST:
            _add_level_and_select(request, data)
            form = CourseForm(data, request.FILES)
            return render(request, 'courses/create_course.html', {'form': form})

        form = CourseForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Course created successfully.")
            return redirect('courses:course_list')
        messages.error(
            request,
            "There was an error creating the course."
            "Please check the form and try again."
        )
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


@login_required
def update_level(request, pk):
    if not request.user.is_superuser:
        messages.error(request, "You do not have permission to update levels.")
        return redirect('courses:course_list')

    level = get_object_or_404(Level, pk=pk)

    if request.method == 'POST':
        form = LevelForm(request.POST, instance=level)
        if form.is_valid():
            form.save()
            messages.success(request, "Level updated successfully.")
            return redirect('courses:admin_dashboard')
        else:
            messages.error(request, "There was an error updating the level. Please check the form and try again.")
    else:
        form = LevelForm(instance=level)

    return render(request, 'courses/update_level.html', {
        'form': form,
        'level': level
    })


@login_required
def update_supply(request, pk):
    if not request.user.is_superuser:
        messages.error(request, "You do not have permission to update supply items.")
        return redirect('courses:course_list')

    supply = get_object_or_404(SupplyItem, pk=pk)

    if request.method == 'POST':
        form = SupplyItemForm(request.POST, instance=supply)
        if form.is_valid():
            form.save()
            messages.success(request, "Supply item updated successfully.")
            return redirect('courses:admin_dashboard')
        else:
            messages.error(request, "There was an error updating the supply item. Please check the form and try again.")
    else:
        form = SupplyItemForm(instance=supply)

    return render(request, 'courses/update_supply.html', {
        'form': form,
        'supply': supply
    })


@login_required
def delete_level(request, pk):
    if not request.user.is_superuser:
        messages.error(request, "You do not have permission to delete levels.")
        return redirect('courses:course_list')
    level = get_object_or_404(Level, pk=pk)
    if request.method == 'POST':
        level.delete()
        messages.success(request, "Level deleted successfully.")
        return redirect('courses:admin_dashboard')
    return render(request, 'courses/delete_level.html', {'level': level})


@login_required
def delete_supply(request, pk):
    if not request.user.is_superuser:
        messages.error(request, "You do not have permission to delete supply items.")
        return redirect('courses:course_list')
    supply = get_object_or_404(SupplyItem, pk=pk)
    if request.method == 'POST':
        supply.delete()
        messages.success(request, "Supply item deleted successfully.")
        return redirect('courses:admin_dashboard')
    return render(request, 'courses/delete_supply.html', {'supply': supply})


@login_required
def admin_dashboard(request):
    if not request.user.is_superuser:
        messages.error(request, "You do not have permission to access this page.")
        return redirect('courses:course_list')

    levels = Level.objects.all()
    supplies = SupplyItem.objects.all()
    courses = Course.objects.all()
    return render(request, 'courses/admin_dashboard.html', {
        'levels': levels,
        'supplies': supplies,
        'courses': courses
    })
