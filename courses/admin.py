from django.contrib import admin
from .models import Level, SupplyItem, Course

# Register your models here.
admin.site.register(Level)
admin.site.register(SupplyItem)


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("name", "level", "price", "max_participants")
    list_filter = ("level",)
    search_fields = ("name", "description")
