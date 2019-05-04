"""
Copyright 2019 Chain Gang Entertainment Inc. All Rights Reserved.
Original Author: Russ 'trdwll' Treadwell <russ@trdwll.com>
""" 
from django import forms

class ContactForm(forms.Form):
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'Email'
    }), min_length=10, label='Email', required=True, help_text='What\'s your email address so we can contact you if needed.')

    title = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Title'
    }), min_length=10, label='Title', required=True, help_text='Title of the email that you\'re sending us.')

    content = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control',
        'id': 'editor',
    }), required=False, label='Body', help_text='')

    meta = [
        'email',
        'title',
        'content'
    ]