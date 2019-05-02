
from django.urls import path

from . import views


urlpatterns = [
    path('', views.StoreHomeView.as_view(), name='store_home'),
]