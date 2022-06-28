from django.contrib import admin

from .models import (
    Course
)


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['instructor', 'course_name', 'published_date', 'updated_on']
