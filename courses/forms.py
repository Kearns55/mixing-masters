from django import forms
from .models import Course, Level, SupplyItem


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = "__all__"
class LevelForm(forms.ModelForm):

    class Meta:
        model = Level
        fields = "__all__"


class SupplyItemForm(forms.ModelForm):

    class Meta:
        model = SupplyItem
        fields = "__all__"
