from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import Course, Purchase
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