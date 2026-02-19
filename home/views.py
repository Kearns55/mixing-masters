from django.shortcuts import render
from courses.models import Course
# Create your views here.


def home(request):
    courses = Course.objects.filter(is_active=True)
    context = {
        'courses': courses,
    }
    return render(request, 'home/index.html', context)
