from django.urls import path
from . import views


app_name = "courses"

urlpatterns = [
    path('', views.CourseList.as_view(), name='course_list'),
    path('<int:pk>/', views.CourseDetail.as_view(), name='course_detail'),
    path('<int:pk>/checkout/', views.create_checkout_session, name='create_checkout_session'),
    path('my-courses/', views.my_courses, name='my_courses'),
    path('create-course/', views.create_course, name='create_course'),
    path('update-course/<int:pk>/', views.update_course, name='update_course'),
    path('delete-course/<int:pk>/', views.delete_course, name='delete_course'),
    path('success/', views.payment_success, name='payment_success'),
    path('cancel/', views.payment_cancel, name='payment_cancel'),
]
