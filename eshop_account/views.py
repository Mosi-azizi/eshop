from django.shortcuts import render, redirect
from .forms import LoginForm,RegisterForm
from django.contrib.auth import login,authenticate,get_user_model
from django.contrib.auth.models import User
# Create your views here.

def login_user(request):
    if request.user.is_authenticated:
        return redirect('/')

    login_form =LoginForm(request.POST or None)
    if login_form.is_valid():
        user_name = login_form.cleaned_data.get('user_name')
        password = login_form.cleaned_data.get('password')
        # print(user_name)
        # print(password)
        user=authenticate(request,username=user_name,password=password)
        if user is not None:
            login(request,user)
            return redirect('/')

    context = {
        'login_form':login_form
    }
    return  render(request,'account/login.html',context)

def register(request):
    if request.user.is_authenticated:
        return  redirect("/")
    register_form = RegisterForm(request.POST or None)
    if register_form.is_valid():
        user_name = register_form.cleaned_data.get('user_name')
        email = register_form.cleaned_data.get('email')
        password = register_form.cleaned_data.get('password')
        User.objects.create_user(username=user_name,email=email,password=password)
        return redirect('/')

    context = {
    'register_form':register_form
    }
    return  render(request,'account/register.html',context)
