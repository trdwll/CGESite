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