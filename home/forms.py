from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, Post, Donation
#Category
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    ngo = forms.BooleanField(required=False)
    class Meta:
        model = User
        fields = ["username", 'email', 'ngo', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile 
        fields = ['image']
        
# choices = Category.objects.all().values_list('name','name')

# choice_list =[]

# for item in choices:
#     choice_list.append(item)

# class PostForm(forms.ModelForm):
#     class Meta:
#         model= Post
#         fields=('title','category','content')

#         widgets = {

#             'title' : forms.TextInput(attrs={'class':'form-control'}),
#             'category': forms.Select(choices=choice_list,attrs={'class':'form-control'}),
#             'content': forms.Textarea(attrs={'class':'form-control'})
        
#         }

class Form(forms.ModelForm):
    quantity= forms.IntegerField()
    class Meta:
        model= Donation
        fields=('quantity',)
        
# -*- coding: utf-8 -*-

