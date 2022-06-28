from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from user.serializers import TeacherRegisterUserSerializer, StudentRegisterUserSerializer


@api_view(['POST', ])
def register_user_teacher(request):
    if request.method == 'POST':
        serializer = TeacherRegisterUserSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            new_user = serializer.create(serializer.validated_data)
            data['message'] = 'success'
            data['email'] = new_user.email
            data['is_teacher'] = new_user.is_teacher
        else:
            data['message'] = serializer.errors
        return Response(data)


@api_view(['POST', ])
def register_user_student(request):
    if request.method == 'POST':
        serializer = StudentRegisterUserSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            new_user = serializer.create(serializer.validated_data)
            data['message'] = 'success'
            data['email'] = new_user.email
            data['is_student'] = new_user.is_student
        else:
            data['message'] = serializer.errors
        return Response(data)
