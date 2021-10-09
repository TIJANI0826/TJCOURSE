from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import student, teachers
# app_name = 'simplecourse'
urlpatterns = [
    path('', student.home ),
    path('course/<int:pk>/', student.CourseDetailView.as_view(), name='course-detail'),
    path('teacher/<int:pk>/', teachers.TeacherDetailView.as_view(), name='teacher-detail'),

    path('student_register', student.StudentSignUpView.as_view(), name='student_signup'),
    path('teacher_register',teachers.TeacherSignUpView.as_view(),name='teacher_signup'),

]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)