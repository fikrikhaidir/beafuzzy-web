from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import UserLoginForm,UserRegisterForm


def homepage(request):
    akun = request.user
    if akun.is_authenticated():
        return redirect('dashboard:home')
    else:
        title="login"
        formLogin = UserLoginForm(request.POST or None)
        if formLogin.is_valid():
            username = formLogin.cleaned_data.get("username")
            password = formLogin.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            login(request,user)
            return redirect('dashboard:home')
    return render(request,"landing/home.html",{"formLog":formLogin,"title":title})


def register(request):
    title = 'Register'
    formRegister = UserRegisterForm(request.POST or None)
    if formRegister.is_valid():
        user = formRegister.save(commit=False)
        password = formRegister.cleaned_data.get('password')
        user.set_password(password)
        user.save()
        n_user=authenticate(username=user.username,password=password)
        login(request,n_user)
        return HttpResponseRedirect('../dashboard')
    formLogin = UserLoginForm(request.POST or None)
    if formLogin.is_valid():
        username = formLogin.cleaned_data.get("username")
        password = formLogin.cleaned_data.get("password")
        user = authenticate(username=username, password=password)
        login(request,user)
        return redirect('dashboard:home')

    return render(request,"landing/register.html",{"title":title,"formLog":formLogin,"formReg":formRegister})

def Logout(request):
    logout(request)
    return HttpResponseRedirect('/')

def about(request):
    context ={}
    return render(request,"landing/about.html",(context))
