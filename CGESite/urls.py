"""
Copyright 2019 Film And Music Inc. All Rights Reserved.
Original Author: Russ 'trdwll' Treadwell <russ@trdwll.com>
""" 

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from django.contrib.auth.views import LogoutView

#from paypal.express.dashboard.app import application as paypal_application

from . import views
from users.views import LoginView, RegisterView, SettingsView
from store.views import PurchasesView


urlpatterns = [
    path('', views.HomeView.as_view(), name='home_page'),
    path('contact/', views.ContactView.as_view(), name='contact_page'),

    path('forum/', include('forum.urls')),
    path('store/', include('store.urls')),

    #path('store/checkout/paypal/', include('paypal.express.urls')),
    #path('store/dashboard/paypal/express/', paypal_application.urls),
    path('i18n/', include('django.conf.urls.i18n')),

    path('blog/', include('blog.urls')),

    path('auth/login/', LoginView.as_view(), name='login'),
    path('auth/register/', RegisterView.as_view(), name='register'),
    path('auth/logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('settings/', SettingsView.as_view(), name='settings'),
    path('settings/purchases/', PurchasesView.as_view(), name='purchases'),

    #path('auth/recover/', RecoverView.as_view(), name='user_recover_page'),
    #path('auth/recover/step2/', RecoverTokenView.as_view(), name='user_token_page'),

    path('auth/', include('social_django.urls', namespace='social')),

    path('admin/', admin.site.urls),
    path('dev/', TemplateView.as_view(template_name='developer.html')),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


admin.site.site_header = 'Chain Gang Entertainment Inc AdminCP'
admin.site.site_title = 'Chain Gang Entertainment Inc AdminCP'

# admin.site.__class__ = OTPAdminSite