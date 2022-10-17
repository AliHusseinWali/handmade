from tokenize import group
from django.shortcuts import redirect
from django.urls import reverse

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
