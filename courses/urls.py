from django.urls import path
from . import views


app_name = "courses"

urlpatterns = [
    path('', views.CourseList.as_view(), name='course_list'),
    path('<int:pk>/', views.CourseDetail.as_view(), name='course_detail'),
]
