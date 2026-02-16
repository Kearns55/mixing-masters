from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Course

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
