from django import forms
from django.utils import timezone
from datetime import timedelta
from .models import Course, Level, SupplyItem


class CourseForm(forms.ModelForm):

    class Meta:
        model = Course
        fields = "__all__"
        widgets = {
            "start_date": forms.DateTimeInput(
                attrs={
                    "type": "datetime-local",
                }
            )
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        tomorrow = (timezone.now() + timedelta(days=1)).strftime("%Y-%m-%dT%H:%M")

        # Prevent selecting dates before tomorrow
        self.fields["start_date"].widget.attrs["min"] = tomorrow


class LevelForm(forms.ModelForm):

    class Meta:
        model = Level
        fields = "__all__"


class SupplyItemForm(forms.ModelForm):

    class Meta:
        model = SupplyItem
        fields = "__all__"
