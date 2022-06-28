from rest_framework import serializers
from .models import CourseRegistration
from teacher.models import Course


class CourseRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseRegistration
        fields = ('course', 'student', 'registration_date', 'subscribed')


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')
