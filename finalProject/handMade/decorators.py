from tokenize import group
from django.shortcuts import redirect, render
from django.urls import reverse
from .models import Categories

def notLoggedUsers(viewFunction):
    def wrapperFunction(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        else:
            return viewFunction(request, *args, **kwargs)
    return wrapperFunction

def forAdmin(viewFunction):
    def wrapperFunction(request, *args, **kwargs):
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name
        if group == 'Admin':
            return viewFunction(request, *args, **kwargs)
        if group == 'customers':
            return redirect(reverse('home'))
    return wrapperFunction

def allowedUsers(allowedGroups=[]):
    def decorator(view_func):
        def wrapper_func(request , *args , **kwargs):
            group = None
            if request.user.groups.exists():
               group = request.user.groups.all()[0].name
            if group in allowedGroups:
               return view_func(request , *args , **kwargs)
            else:
                return redirect('user/')
        return wrapper_func
    return decorator        