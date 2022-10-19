from tokenize import blank_re
from django.db import models
from django.contrib.auth.models import User
from django.db import models



# Create your models here.


class Customer(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=True)
    email = models.EmailField(max_length=100, null=True)
    phone = models.CharField(max_length=15)
    photo = models.ImageField(default="")

    def __str__(self):
        return self.name


class Categories(models.Model):
    title = models.ForeignKey('self', related_name='children' ,on_delete=models.CASCADE,db_column="Main category" ,null=True,blank=True)
    sub_category = models.CharField(max_length=200, db_column="Sub category", null=True)


    def __str__(self):
        return self.title

    def __str__(self):
        main_category = [self.sub_category]                  
        Sub = self.title
        while Sub is not None:
            main_category.append(Sub.sub_category)
            Sub = Sub.title
        return ' -> '.join(main_category[::-1])  



class Product (models.Model):
    title = models.CharField(max_length=500, verbose_name="name of Products")
    description = models.TextField(max_length=1000)
    imageLink = models.CharField(max_length=500, null=True)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE, null=True)
    price = models.FloatField(max_length=50)
    availability = models.BooleanField(default=True)
    favorite = models.ManyToManyField(User, blank=True)
    cart = models.ManyToManyField(User,blank=True,related_name='Cart')

    def __str__(self):
        return f"{self.title}:{self.description}"