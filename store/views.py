from django.shortcuts import render, redirect
from django.views.generic import View, ListView
from django.shortcuts import render, get_object_or_404, get_list_or_404

from .models import Product

class StoreHomeView(ListView):
    model = Product
    template_name = 'store/index.html'
    paginate_by = 5
    context_object_name = 'products'