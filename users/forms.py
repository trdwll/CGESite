"""
Copyright 2019 Chain Gang Entertainment Inc. All Rights Reserved.
Original Author: Russ 'trdwll' Treadwell <russ@trdwll.com>
""" 

from django import forms
from django.contrib.auth.models import User

#from .models import UserProfile


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control form-control-secondary',
            'placeholder': 'Username'
        }), min_length=2, label='Username', required=True, help_text='The username of your account.')

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control form-control-secondary', 
            'value': '', 
            'placeholder': 'Password'
        }), min_length=8, label='Password', required=True, help_text='The password that you use to sign in your account.')

    class Meta:
        fields = [
            'username',
            'password'
        ]


class RegisterForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control form-control-secondary',
            'placeholder': 'Username'
        }), min_length=2, label='Username', required=True, help_text='Username that will be displayed around the website.')

    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'form-control form-control-secondary',
            'placeholder': 'Email'
        }), label='Email', required=True, help_text='We\'ll never share your email with anyone else.')

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control', 
            'value': '', 
            'placeholder': 'Password'
        }), min_length=8, label='Password', required=True, help_text='The password that you\'ll use to sign in your account.')
    
    password_confirm = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control', 
            'value': '', 
            'placeholder': 'Confirm Password'
        }), min_length=8, label='Password', required=True, help_text='The password that you\'ll use to sign in your account.')

    class Meta:
        fields = [
            'username',
            'email',
            'password',
            'password_confirm'
        ]
