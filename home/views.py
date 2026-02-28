from django.shortcuts import render
from courses.models import Course


def homepage(request):
    latest_courses = Course.objects.order_by('-created_at')[:3]
    return render(request, "home/index.html", {
        "latest_courses": latest_courses
    })