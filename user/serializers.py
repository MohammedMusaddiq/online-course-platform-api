from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class TeacherRegisterUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password', 'is_teacher')
        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }

    def create(self, validated_data):
        return User.objects.create_user(email=self.validated_data['username'], password=self.validated_data['password'],
                                        is_teacher=True)


class StudentRegisterUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password', 'is_student')
        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }

    def create(self, validated_data):
        return User.objects.create_user(email=self.validated_data['username'], password=self.validated_data['password'],
                                        is_student=True)
