from django.urls import path
from . import views

urlpatterns = [
    path('', views.home , name='home'),
    path('login', views.userLogin , name='login'),
    path('register', views.register , name='register'),
    path('addProduct', views.addProduct , name='addProduct'),
    path('cart', views.cart , name='cart'),
    path('favorite', views.favorite , name='favorite'),
    # path('allProduct', views.allProduct , name='allProduct'),
]
