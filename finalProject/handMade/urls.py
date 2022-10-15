from django.urls import path
from . import views

urlpatterns = [
    path('', views.home , name='home'),
    path('login', views.userLogin , name='login'),
    path('register', views.register , name='register'),
    path('addProduct', views.addProduct , name='addProduct'),
    path('cart', views.cart , name='cart'),
    path('favorite', views.user_favorites , name='user_favorites'),
    path('Product_details/<int:id>', views.product_details , name='Product_details'),
    path('add_remove_favorite/<int:id>', views.add_remove_favorite , name='add_remove_favorite'),


]
