from . import views
from django.urls import path

urlpatterns = [
    path('', views.CourseList.as_view(), name='home'),
]
