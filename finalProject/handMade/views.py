from itertools import product
from unicodedata import category
from django.shortcuts import redirect, render
from .form import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import  HttpResponseRedirect
from django.urls import reverse
from django.db import IntegrityError
from.decorators import forAdmin, notLoggedUsers
from .models import *


# Create your views here.


def home(request):
    categories = Categories.objects.filter(title=None)
    product = Product.objects.all()

    name = None
    desc = None
    PriceFrom = None
    PriceTo = None
    caseSensitive = None
    
    if 'cs' in request.GET:
        caseSensitive = request.GET['cs']
        if not caseSensitive:
            caseSensitive = 'off'
    
    if 'searchname' in request.GET:
        name = request.GET['searchname']
        if name:
            if caseSensitive=='on':
                product = product.filter(title__contains=name)
            else:
                product = product.filter(title__icontains=name)
                
    if 'searchdesc' in request.GET: 
        desc = request.GET['searchdesc']
        if desc:
            if caseSensitive=='on':
                product = product.filter(description__contains=desc)
            else:
                product = product.filter(description__icontains=desc)

    if 'searchpricefrom' in request.GET and 'searchpriceto' in request.GET:
        PriceFrom = request.GET['searchpricefrom']
        PriceTo = request.GET['searchpriceto']
        if PriceFrom and PriceTo:
            if PriceFrom.isdigit() and PriceTo.isdigit():
                product = product.filter( price__gte=PriceFrom , price__lte=PriceTo )

    if 'searchall' in request.GET:
        name = request.GET['searchall']
        if name:
            product = product.filter(title__contains=name) | product.filter(description__contains=name) | product.filter(price__contains=name)
            
    return render(request, 'handMade/allProduct.html',{'product':product,'categories':categories})


def add_remove_favorite(request,id):
    product = Product.objects.get(id=id)
    if request.user in product.favorite.all():
        product.favorite.remove(request.user)
    else:
        product.favorite.add(request.user)
    return redirect(reverse('home'))


@notLoggedUsers
def userLogin(request):
    categories = Categories.objects.filter(title=None)
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Credentials error')
    return render(request, 'handMade/login.html',{'categories':categories})

def userLogout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))


@notLoggedUsers
def register(request):
    categories = Categories.objects.filter(title=None)
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
        return render(request, 'handMade/register.html',{'categories':categories})

@forAdmin
def addProduct(request):
    categories = Categories.objects.filter(title=None)

    if request.method =='POST':
        form = AddProduct(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("home"))
        else:
            return render(request, "handMade/addproduct.html",{'form':form})
    else:
        context = {
            'form':AddProduct(),
            'categories':categories
        }
        return render(request,'handMade/addProduct.html', context)

def cart_for_user(request):
    categories = Categories.objects.filter(title=None)
    userCart = Product.objects.filter(cart=request.user)
    context = {
        'userCart':userCart,
        'categories':categories
    }
    return render(request, 'handMade/cart.html',context)

def user_favorites(request):
    categories = Categories.objects.filter(title=None)
    user_favorites = Product.objects.filter(favorite=request.user)
    context = {
        'user_favorites':user_favorites,
        'categories':categories
    }
    return render(request, 'handMade/favorite.html',context)

def product_details(request,id):
    categories = Categories.objects.filter(title=None)
    product = Product.objects.get(pk=id)
    context = {
        'product':product,
        'categories':categories
    }
    return render(request, 'handMade/product_details.html',context)

def add_remove_to_cart(request,id):
    product = Product.objects.get(pk=id)
    if request.user in product.cart.all():
        product.cart.remove(request.user)
    else:
        product.cart.add(request.user)
    return redirect(reverse('Product_details', kwargs={'id':product.id}))



def search(request):
    return render(request,'handMade/search.html' )

def categoreis(request):
    categories = Categories.objects.filter(title=None)
    categoriesall = Categories.objects.all()
    return render(request,'handMade/category.html',{'categoreisall':categoriesall.sub_category,'categoreisa':categories})

def chooes_category(request,id):
    # category = Categories.objects.get(id=id)
    # return render(request,'handMade/note_cat.html',{'category':category.sub_category})
    
    category = Categories.objects.get(id=id)
    category_user = Categories.objects.filter(pk=id).prefetch_related('children__product_set',).get()
    product = Product.objects.filter(category=category_user)
    child_products = Product.objects.filter(category__in=category_user.children.all())
    all_products = product.union(child_products)
    context = {
        'category_user':category_user,
        'all_products':all_products,
        'category':category
    }
    return render(request,'handMade/note_cat.html',context)