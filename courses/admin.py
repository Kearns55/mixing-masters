from django.contrib import admin
from .models import Level, SupplyItem, Course, Purchase
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
admin.site.register(Level)
admin.site.register(SupplyItem)
admin.site.register(Purchase)


@admin.register(Course)
class CourseAdmin(SummernoteModelAdmin):
    list_display = ('name', 'level', 'start_date', 'location', 'price', 'max_participants', 'is_active')
    list_filter = ('level', 'is_active')
    search_fields = ('name', 'description', 'location')
    summernote_fields = ('description',)

