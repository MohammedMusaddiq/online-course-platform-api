from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Course

User = get_user_model()


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'
