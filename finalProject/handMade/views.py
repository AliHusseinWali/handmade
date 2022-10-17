from math import prod
from re import A
from shutil import register_unpack_format
from xml.sax.handler import property_declaration_handler
from click import confirmation_option
from django.forms import IntegerField
from django.shortcuts import redirect, render
from .form import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import  HttpResponseRedirect
from django.urls import reverse
from django.db import IntegrityError
from.decorators import forAdmin, notLoggedUsers


# Create your views here.


def home(request):
    product = Product.objects.all()
    return render(request, 'handMade/allProduct.html',{'product':product})
    # return render(request,"handMade/home.html")


def add_remove_favorite(request,id):
    product = Product.objects.get(id=id)
    if request.user in product.favorite.all():
        product.favorite.remove(request.user)
    else:
        product.favorite.add(request.user)
    return redirect(reverse('home'))
    # return redirect('home')

@notLoggedUsers
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

def userLogout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))


@notLoggedUsers
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']

        password = request.POST['password']
        confirmation = request.POST['confirmation']
        if password != confirmation:
            return render(request, 'handMade/register.html',{
                'message': 'Passwords must match.'
            })
        try:
            user = User.objects.create_user(username, email, password)
        except IntegrityError:
            return render(request, 'handMade/register.html',{
                'message': 'Username already taken.'
            })
        login(request, user)
        return HttpResponseRedirect(reverse('home'))
    else:
        return render(request, 'handMade/register.html')
@forAdmin
def addProduct(request):
    if request.method =='POST':
        form = AddProduct(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("home"))
        else:
            return render(request, "handMade/addproduct.html",{'form':form})
    else:
        return render(request,'handMade/addProduct.html',{'form':AddProduct()})

def cart(request):
    return render(request, 'handMade/cart.html')


def user_favorites(request):
    user_favorites = Product.objects.filter(favorite=request.user)
    return render(request, 'handMade/favorite.html',{'user_favorites':user_favorites})

def product_details(request,id):
    product = Product.objects.get(pk=id)
    return render(request, 'handMade/product_details.html',{'product':product})


