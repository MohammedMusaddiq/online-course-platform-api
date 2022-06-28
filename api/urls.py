from django.urls import path
from rest_framework.authtoken import views
import student.views as s
import teacher.views as t
import user.views as u

app_name = 'api'

urlpatterns = [
    # authentication  endpoints
    path('user/teacher/register/', u.register_user_teacher, name='register-user-teacher'),
    path('user/student/register/', u.register_user_student, name='register-user-student'),
    path('user/login/', views.obtain_auth_token, name='login'),

    # teacher app endpoints
    path('teacher/courses/', t.course_list, name='teacher-courses'),
    path('teacher/create-course/', t.create_course, name='create-course'),
    path('teacher/student-list/', t.student_list, name='student-list'),

    # student app endpoints
    path('student/explore/', s.explore_courses, name='explore-courses'),
    path('student/subscribe-to-course/', s.subscribe_to_course, name='subscribe-to-course'),
    path('student/unsubscribe/', s.unsubscribe, name='unsubscribe'),
    path('student/subscribed-courses/', s.subscribe_course, name='subscribed-courses'),
]
