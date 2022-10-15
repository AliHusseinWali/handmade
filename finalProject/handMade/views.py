from math import prod
from re import A
from shutil import register_unpack_format
from xml.sax.handler import property_declaration_handler
from django.shortcuts import redirect, render
from .form import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import  HttpResponseRedirect
from django.urls import reverse

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
    # return redirect(reverse('home'))
    return redirect('home')


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
            messages.success(request, username + ' Created Successfully !')
            return redirect('login')
        else: 
            messages.error(request, 'invalid')
    return render(request,"handMade/register.html",{'form':form})


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


