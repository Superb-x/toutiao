from django.shortcuts import render, render_to_response, redirect
from django.contrib.auth.hashers import make_password, check_password
from django.http import HttpResponse
from django import forms
from .models import User

# Create your views here.
class UserForm(forms.Form):
    username = forms.CharField(label='用户名', max_length=50)
    password = forms.CharField(label='密码', widget=forms.PasswordInput())
    email = forms.EmailField(label='邮箱')

def index(request):
    context = {'text': 'hello, world!'}
    return render(request, 'news/index.html', context)

def register(request):
    if request.method == 'POST':
        userform = UserForm(request.POST)
        if userform.is_valid():
            username = userform.cleaned_data['username']
            password = userform.cleaned_data['password']
            email = userform.cleaned_data['email']
            pwd = make_password(password)

            u = User.objects.filter(username__exact=username)
            if u:
                return HttpResponse('该用户名已经存在!')
            else:
                user = User.objects.create(username=username, password=pwd, email=email)
                user.save()

                return HttpResponse('恭喜您，注册成功!!!')
    else:
        userform = UserForm()
    return render_to_response('news/register.html', {'userform': userform})

def login(request):
    if request.method == 'POST':
        userform = UserForm(request.POST)
        if userform.is_valid():
            username = userform.cleaned_data['username']
            password = userform.cleaned_data['password']
            pwd = User.objects.filter(username=username).values('password')
            pwd = list(pwd)[0]['password']
            print(check_password(password, pwd))
            if check_password(password, pwd):
                context = {'text': username}
                return render_to_response('news/index.html', context)
            else:
                return HttpResponse('用户名或者密码错误,请重新登录')
    else:
        userform = UserForm()

    return render_to_response('news/login.html', {'userform': userform})
