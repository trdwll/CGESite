from django.shortcuts import render, render_to_response, get_object_or_404, get_list_or_404
from django.views.generic import View, ListView

from django.db.models import Avg

from .models import StoreItem, Category, Coupon

class StoreHomeView(ListView):
    model = StoreItem
    template_name = 'store/store-home-page.html'
    paginate_by = 50

    # could probably zip this list with the average_ratings list...
    def get_queryset(self, *args, **kwargs):
        return get_list_or_404(StoreItem.objects.order_by('price'), is_visible=True)


class StoreItemView(View):
    template_name = 'store/store-item-page.html'

    def get(self, request, slug):
        item = get_object_or_404(StoreItem.objects.filter(is_visible=True, slug=slug))

        return render(request, self.template_name, {
            'item': item, 
        })


class StoreItemCategoryView(ListView):
    model = Category
    template_name = 'store/store-category-item-page.html'
    paginate_by = 50

    def get_queryset(self, *args, **kwargs):
        category = get_object_or_404(Category.objects.filter(slug=self.kwargs['slug']))
        return get_list_or_404(StoreItem.objects.filter(category=category, is_visible=True))