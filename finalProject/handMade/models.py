from contextlib import nullcontext
from email.policy import default
from pydoc import describe
from unicodedata import category
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Customer(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=True)
    email = models.EmailField(max_length=100, null=True)
    phoneNumber = models.IntegerField(max_length=50, null=True)
    photo = models.ImageField(default="")

    def __str__(self):
        return self.name


class Categories(models.Model):
    name = models.CharField(max_length=200, db_column="Catogery", null=True)

    def __str__(self):
        return self.name


class Product (models.Model):
    title = models.CharField(max_length=500, verbose_name="name of Products")
    description = models.TextField(max_length=1000)
    imageLink = models.CharField(max_length=500, null=True)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE, null=True)
    price = models.FloatField(max_length=50)
    availability = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.title}:{self.description}"