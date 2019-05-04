"""
Copyright 2019 Chain Gang Entertainment Inc. All Rights Reserved.
Original Author: Russ 'trdwll' Treadwell <russ@trdwll.com>
""" 
from django import forms

from .models import Topic, Post


class CreateTopicForm(forms.Form):
    title = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Title'
    }), min_length=10, label='Title', required=True, help_text='Title of your topic.')

    content = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control',
        'id': 'editor',
    }), required=False, label='Body', help_text='')

    meta = [
        'title',
        'content'
    ]


class ReplyTopicForm(forms.Form):
    content = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control',
        'id': 'editor',
    }), required=False, label='Body', help_text='')

    meta = [
        'content'
    ]