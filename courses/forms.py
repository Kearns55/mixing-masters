from django import forms
from .models import Course, Level, SupplyItem


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = "__all__"
