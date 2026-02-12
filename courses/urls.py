from . import views
from django.urls import path

urlpatterns = [
    path('', views.Homepage.as_view(), name='homepage-urls'),
    path('courses/', views.CourseList.as_view(), name='courses-urls'),
]
