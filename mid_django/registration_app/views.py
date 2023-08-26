from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import models
# Create your views here.


def SignUp(request):
    return render(request, 'signup.html')

def SignUpDataUpload(request):
    user_name = request.POST.get('user_name')
    user_email = request.POST.get('user_email')
    user_password = request.POST.get('user_password')
    user_object = models.User()
    user_object.username = user_name
    user_object.email = user_email
    user_object.password = user_password
    user_object.save()
    return HttpResponse("sign up success")


def Login(request):
    return render(request, 'login.html')
