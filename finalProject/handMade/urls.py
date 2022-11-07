from django.urls import path
from . import views

urlpatterns = [
    path('', views.home , name='home'),
    path('login', views.userLogin , name='login'),
    path('logout', views.userLogout , name='logout'),
    path('register', views.register , name='register'),
    path('addProduct', views.addProduct , name='addProduct'),
    path('cart', views.cart_for_user , name='cart'),
    path('favorite', views.user_favorites , name='user_favorites'),
    path('Product_details/<int:id>', views.product_details , name='Product_details'),
    path('add_remove_favorite/<int:id>', views.add_remove_favorite , name='add_remove_favorite'),
    path('add_remove_to_cart/<int:id>', views.add_remove_to_cart , name='add_remove_to_cart'),
    path('search', views.search , name='search'),
    path('category', views.categoreis , name='categoreis'),
    path('category/<int:id>', views.chooes_category , name='chooes_category'),
    path('add_quantity/<int:id>', views.add_quantity , name='add_quantity'),
    path('sub_quantity/<int:id>', views.sub_quantity , name='sub_quantity'),
    path('contact', views.contact , name='contact'),

    


]
