from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from .models import CourseRegistration
from teacher.models import Course
from .serializers import CourseRegistrationSerializer, CourseSerializer


@api_view(['GET', ])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def subscribe_course(request):
    subscribed_courses = CourseRegistration.objects.filter(student_id=request.user.id)
    data = {}
    if len(subscribed_courses) > 0:
        serializer = CourseRegistrationSerializer(subscribed_courses, many=True)
        data['result'] = serializer.data
    else:
        data['message'] = "No courses subscribed yet"
    return Response(data)


@api_view(['GET', ])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def explore_courses(request):
    course_list = Course.objects.all().order_by('-updated_on')
    serializer = CourseSerializer(course_list, many=True).data
    return Response(serializer)


@api_view(['POST', ])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def subscribe_to_course(request):
    course_id = request.POST.get('id')
    course = Course.objects.get(id=course_id)
    course_registration = CourseRegistration.objects.create(course=course, student=request.user, subscribed=True)
    serializer = CourseRegistrationSerializer(course_registration)
    return Response(serializer.data)


@api_view(['POST', ])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def unsubscribe(request):
    course_reg_id = request.POST.get('id')
    course_registration = CourseRegistration.objects.get(id=course_reg_id)
    course_registration.delete()
    return Response({"message": "Course Unsubscribe Successfully"})
