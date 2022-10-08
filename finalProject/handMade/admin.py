from django.contrib import admin
from .models import *
# Register your models here.

class customerAdmin(admin.ModelAdmin):
    list_display = ('user','name', 'email','phone','photo')

class productAdmin(admin.ModelAdmin):
    list_display =  ('title','description','imageLink', 'category','price','availability')

admin.site.register(Customer,customerAdmin)
admin.site.register(Categories)
admin.site.register(Product,productAdmin)
