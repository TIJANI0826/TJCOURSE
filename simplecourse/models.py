from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.deletion import DO_NOTHING
from django.urls import reverse
from django.contrib.auth.models import AbstractUser

# Create your models here.
def user_directory_path(instance,filename):
    return 'user_{0}/{1}'.format(instance.user.id,filename)


class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    
    # User reputation score.

    def __str__(self):
        return self.user.username
    
    def get_absolute_url(self):
        return reverse('student-detail', args=[str(self.id)])

class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    
    # User reputation score.

    def __str__(self):
        return self.user.username
    
    def get_absolute_url(self):
        return reverse('teacher-detail', args=[str(self.user.id)])

class Course(models.Model):
    user = models.ForeignKey(
        get_user_model(),
        null=True,
        on_delete=DO_NOTHING
    )
    course_title = models.CharField(max_length=250,verbose_name="COURSE TITLE")
    course_date_created = models.DateTimeField(auto_now_add=True)
    course_image = models.ImageField(upload_to=user_directory_path)
    course_description = models.CharField(max_length=400)
    course_duration = models.IntegerField()
    course_discount = models.IntegerField()
    course_price =  models.IntegerField(default=100)

    def get_absolute_url(self):
        return reverse('course-detail', args=[str(self.id)])

    def __str__(self) -> str:
        return self.course_title