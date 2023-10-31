from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.contrib.auth.models import auth
from django.http import HttpResponseRedirect
from django.shortcuts import render


def register(request):
    if request.method == 'GET':
        return render(request, 'user/register.html')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        password = make_password(password)
        User.objects.create(username=username, password=password)
        return HttpResponseRedirect('/user/login/')


def login(request):
    if request.method == 'GET':
        return render(request, 'user/login.html')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        if user:
            auth.login(request, user)
            return HttpResponseRedirect('/blog')
        else:
            return render(request, 'user/login.html')


def logout(request):
    if request.method == 'GET':
        auth.logout(request)
    return HttpResponseRedirect('/')
