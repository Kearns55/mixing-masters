from django.urls import path
from . import views


app_name = "courses"

urlpatterns = [
    path('', views.CourseList.as_view(), name='course_list'),
    path('<int:pk>/', views.CourseDetail.as_view(), name='course_detail'),
    path('<int:pk>/checkout/', views.create_checkout_session,
         name='create_checkout_session'),
    path('my-courses/', views.my_courses, name='my_courses'),
    path('create-course/', views.create_course, name='create_course'),
    path('update-course/<int:pk>/', views.update_course, name='update_course'),
    path('delete-course/<int:pk>/', views.delete_course, name='delete_course'),
    path('success/', views.payment_success, name='payment_success'),
    path('cancel/', views.payment_cancel, name='payment_cancel'),
    path('update-level/<int:pk>/', views.update_level, name='update_level'),
    path('delete-level/<int:pk>/', views.delete_level, name='delete_level'),
    path('update-supply/<int:pk>/', views.update_supply, name='update_supply'),
    path('delete-supply/<int:pk>/', views.delete_supply, name='delete_supply'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
]
