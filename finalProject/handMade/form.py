from dataclasses import field
from django.forms import ModelForm
from .models import Customer
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = "__all__"


class CreateNewUser(UserCreationForm):
    class Meta:
        model = User
        # field = "__all__"
        fields = ['username','email','password1','password2']
