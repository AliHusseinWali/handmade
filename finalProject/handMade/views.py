from django.shortcuts import redirect, render
from .form import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
# Create your views here.


def home(request):
    return render(request,"handMade/home.html")

def userLogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Credentials error')
    return render(request, 'handMade/login.html',{})

def register(request):
    form = CreateNewUser()
    if request.method == 'POST':
        form = CreateNewUser(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, username + 'Created Successfully !')
            return redirect('login')
        else: 
            messages.error(request, 'invalid')
    return render(request,"handMade/register.html",{'form':form})

