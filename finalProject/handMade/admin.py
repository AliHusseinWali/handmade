from django.contrib import admin
from .models import *
# Register your models here.

class customerAdmin(admin.ModelAdmin):
    list_display = ('user','name', 'email','phone','photo')

class productAdmin(admin.ModelAdmin):
    list_display =  ('title','description','imageLink', 'category','price','availability','quantity')

class categoriesAdmin(admin.ModelAdmin):
    list_display = ('title','sub_category')

admin.site.register(Customer,customerAdmin)
admin.site.register(Categories,categoriesAdmin)
admin.site.register(Product,productAdmin)


class orderAdmin(admin.ModelAdmin):
    list_display = ('customer','product','quantity')

admin.site.register(Order,orderAdmin)

