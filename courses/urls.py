from django.urls import path
from . import views


app_name = "courses"

urlpatterns = [
    path('', views.CourseList.as_view(), name='course_list'),
    path('<int:pk>/', views.CourseDetail.as_view(), name='course_detail'),
    path('<int:pk>/checkout/', views.create_checkout_session, name='create_checkout_session'),
    path('success/', views.payment_success, name='payment_success'),
    path('cancel/', views.payment_cancel, name='payment_cancel'),
]
