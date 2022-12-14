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

"""To include the header and footer and to include any page that wants to be displayed inside it,
as well as the specialized search has been added inside it"""

 

def home(request):
    categories = Categories.objects.filter(title=None)
    product = Product.objects.all()

    name = None
    desc = None
    PriceFrom = None
    PriceTo = None
    caseSensitive = None
    
    # for case sensitive search
    
    if 'cs' in request.GET:
        caseSensitive = request.GET['cs']
        if not caseSensitive:
            caseSensitive = 'off'
    
    # for lookup in name of product
    
    if 'searchname' in request.GET:
        name = request.GET['searchname']
        if name:
            if caseSensitive=='on':
                product = product.filter(title__contains=name)
            else:
                product = product.filter(title__icontains=name)
    
    # for lookup in description of product
                
    if 'searchdesc' in request.GET: 
        desc = request.GET['searchdesc']
        if desc:
            if caseSensitive=='on':
                product = product.filter(description__contains=desc)
            else:
                product = product.filter(description__icontains=desc)

    # for lookup in price of product

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

# add or remove product from favorite list for user

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

# allows the owner of website to add a new product

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

# management the cart that use to buy the product

def cart_for_user(request):
    categories = Categories.objects.filter(title=None)
    userCart = Product.objects.all().filter(cart=request.user)
        
    context = {
        'userCart':userCart,
        'categories':categories,
    }
    return render(request, 'handMade/cart.html',context)

# for add quantity the product that will buy it, when add to cart

def add_quantity(request,id):
    orderUser = Product.objects.get(pk=id)
    if request.user.is_authenticated and not request.user.is_anonymous and id:
        if orderUser.quantity == request.user.id:
            orderUser.quantity +=1
            
            orderUser.save()
        else:
            orderUser.quantity +=1
            orderUser.save()
    return redirect('cart')

# for minimize quantity the product that will buy it, when add to cart

def sub_quantity(request,id):
    orderUser = Product.objects.get(pk=id)
    if request.user.is_authenticated and not request.user.is_anonymous and id:
        if orderUser.quantity == request.user.id:
            if orderUser.quantity > 1:    
                orderUser.quantity -=1
                orderUser.save()
        else:
            orderUser.quantity -=1
            orderUser.save()
    return redirect('cart')

# for management the favorites product  page of for customer

def user_favorites(request):
    categories = Categories.objects.filter(title=None)
    user_favorites = Product.objects.filter(favorite=request.user)
    context = {
        'user_favorites':user_favorites,
        'categories':categories
    }
    return render(request, 'handMade/favorite.html',context)

# view the details of product like title, description, price and image

def product_details(request,id):
    categories = Categories.objects.filter(title=None)
    product = Product.objects.get(pk=id)
    context = {
        'product':product,
        'categories':categories
    }
    return render(request, 'handMade/product_details.html',context)

# add or remove product from cart list for user

def add_remove_to_cart(request,id):
    product = Product.objects.get(pk=id)
    
    if request.user in product.cart.all():
        product.cart.remove(request.user)
    else:
        product.cart.add(request.user)
    return redirect(reverse(
        'Product_details',
        kwargs={'id':product.id}
        ))

#  view advanced search box

def search(request):
    return render(request,'handMade/search.html' )

# views the all categories and sub categories for product

def categoreis(request):
    categories = Categories.objects.filter(title=None)
    return render(request,'handMade/category.html',{'categoreisa':categories})

# to chooes tha any category 

def chooes_category(request,id):
    categories = Categories.objects.filter(title=None)
    category = Categories.objects.get(id=id)
    product = category.product_set.all()
    
    context = {
        'category':category,
        'product':product,
        'categories':categories
    }
    return render(request,'handMade/allProduct.html',context)

def page_not_found_view(request, exception):
    return render(request, 'handMade/404.html', status=404)


def contact(request):
    categories = Categories.objects.filter(title=None)
    context = {
        'categories':categories
    }

    return render(request, 'handMade/contact.html',context)