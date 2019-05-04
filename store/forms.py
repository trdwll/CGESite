"""
Copyright 2019 Chain Gang Entertainment Inc. All Rights Reserved.
Original Author: Russ 'trdwll' Treadwell <russ@trdwll.com>
""" 
from django import forms
from django.utils.translation import gettext_lazy as _

from .models import Order

from localflavor.us.forms import USZipCodeField


PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 6)]

class OrderCreateForm(forms.ModelForm):
    # postal_code = USZipCodeField()

    first_name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'First Name'
        }
    ), min_length=3, label='First Name', required=True)

    last_name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Last Name'
        }
    ), min_length=3, label='Last Name', required=True)

    email = forms.CharField(widget=forms.EmailInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Email'
        }
    ), min_length=10, label='Email', required=True)

    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email']
        # fields = ['first_name', 'last_name', 'email', 'address', 'postal_code', 'city']


class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES, coerce=int, label=_('Quantity'), widget=forms.Select(
        attrs={
            'class': 'selectpicker',
            'data-width': 'fit'
        }
    ))
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)


class CouponApplyForm(forms.Form):
    code = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Coupon Code'
        }
    ), min_length=3, label='')