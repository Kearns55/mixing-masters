from django.shortcuts import render
from django.views import generic
from .models import Course

# Create your views here.


class CourseList(generic.ListView):
    queryset = Course.objects.all()
    template_name = "course_list.html"


class Homepage(generic.TemplateView):
    template_name = "courses/course_detail.html"
    context_object_name = "course"


def homepage(request):
    courses = Course.objects.all()
    return render(request, "home/index.html", {"courses": courses})
