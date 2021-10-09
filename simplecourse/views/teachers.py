from django.shortcuts import render
from ..models import Course, Teacher,Student
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.db.models import Count, Sum
from django.db.models.functions import Concat
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator

from django.views.generic.detail import DetailView
from django.contrib.auth import get_user_model

from django.views.generic import CreateView, ListView, UpdateView
from ..forms import TeacherSignUpForm


User = get_user_model()


class TeacherSignUpView(CreateView):
    model = User
    form_class = TeacherSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'teacher'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/')

class TeacherDetailView(DetailView):
    model = Teacher
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        teachers = Teacher.objects.all()
        courses = Course.objects.all()
        students = Student.objects.all()
        context['teachers'] = teachers
        context['courses'] = courses
        context['students'] = students
        return context