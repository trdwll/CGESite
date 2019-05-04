"""
Copyright 2019 Chain Gang Entertainment Inc. All Rights Reserved.
Original Author: Russ 'trdwll' Treadwell <russ@trdwll.com>
""" 

from django import forms

class NewsletterSubscribeForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control form-control-secondary',
                'placeholder': 'Email'
            }
        ), label='Email', required=True, help_text='We\'ll never share your email with anyone else.')

    class Meta:
        fields = ['email']


class NewsletterUnSubscribeForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control form-control-secondary',
                'placeholder': 'Email'
            }
        ), label='Email', required=True)

    token = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control form-control-secondary',
                'placeholder': 'Token'
            }
        ), min_length=10, label='Token', required=True)

    class Meta:
        fields = ['email', 'token']