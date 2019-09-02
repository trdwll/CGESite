"""
Copyright 2019 Chain Gang Entertainment Inc. All Rights Reserved.
Original Author: Russ 'trdwll' Treadwell <russ@trdwll.com>
""" 
from django import forms


class ReplyPostForm(forms.Form):
    content = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control',
        'id': 'editor',
    }), required=False, label='Body', help_text='')

    meta = [
        'content'
    ]

class ReplyEditPostForm(forms.Form):
    content = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control',
        'id': 'editor',
    }), required=False, label='Body', help_text='')

    update_reason = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Update Reason'
    }), min_length=5, label='Update Reason', required=False)

    meta = [
        'content',
        'update_reason'
    ]
