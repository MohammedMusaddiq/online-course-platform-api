from django.contrib.auth import get_user_model
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response

from student.serializers import CourseRegistrationSerializer
from teacher.models import Course
from student.models import CourseRegistration
from teacher.serializers import CourseSerializer

User = get_user_model()


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def course_list(request):
    courses = Course.objects.filter(instructor_id=request.user.id)
    data = {}
    if len(courses) > 0:
        result = CourseSerializer(courses, many=True)
        data['result'] = result.data
    else:
        data['message'] = "No courses created yet"
    return Response(data)


@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def create_course(request):
    serializer = CourseSerializer(data=request.data)
    data = {}
    if serializer.is_valid():
        course = serializer.save()
        data['instructor_id'] = course.instructor_id
        data['course_name'] = course.course_name
        data['course_description'] = course.course_description
        data['content'] = course.content
    else:
        data['message'] = serializer.errors
    return Response(data)


@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def student_list(request):
    print(request.user.id)
    instructor = User.objects.get(id=request.user.id)
    student_obj = CourseRegistration.objects.filter(course__instructor=instructor)
    serializer = CourseRegistrationSerializer(student_obj, many=True).data
    return Response(serializer)
