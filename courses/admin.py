from django.contrib import admin
from .models import Level, SupplyItem, Course

# Register your models here.
admin.site.register(Level)
admin.site.register(SupplyItem)

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'level', 'start_date', 'location', 'price', 'max_participants', 'is_active')
    list_filter = ('level', 'is_active')
    search_fields = ('name', 'description', 'location')
