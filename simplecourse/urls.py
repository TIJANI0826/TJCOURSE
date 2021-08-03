from django.urls import path
from .views import home,CourseDetailView
from django.conf import settings
from django.conf.urls.static import static
# app_name = 'simplecourse'
urlpatterns = [
    path('', home ),
    path('course/<int:pk>/', CourseDetailView.as_view(), name='course-detail')
]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)