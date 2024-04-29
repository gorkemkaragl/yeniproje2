from django.shortcuts import render,redirect
from django.contrib.auth.models import user
from django.contrib.auth.models 


def index (request):
    if request.user.is_authenticated:
        username= request.user.username
        students = Student.objects.all()
        mean = calculate_mean(students)
        