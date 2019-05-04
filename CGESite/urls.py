"""
Copyright 2019 Chain Gang Entertainment Inc. All Rights Reserved.
Original Author: Russ 'trdwll' Treadwell <russ@trdwll.com>
""" 

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from django.contrib.auth.views import (
    LogoutView, 
    PasswordResetView, 
    PasswordResetDoneView, 
    PasswordResetConfirmView, 
    PasswordResetCompleteView
)


from . import views
from users.views import LoginView, RegisterView, SettingsView
from store.views import PurchasesView
from newsletter.views import NewsletterSubscribeView, NewsletterUnSubscribeView

urlpatterns = [
    path('', views.HomeView.as_view(), name='home_page'),
    path('contact/', views.ContactView.as_view(), name='contact_page'),

    path('forum/', include('forum.urls')),
    path('store/', include('store.urls')),

    path('i18n/', include('django.conf.urls.i18n')),

    path('blog/', include('blog.urls')),

    path('auth/', include('social_django.urls', namespace='social')),
    path('auth/login/', LoginView.as_view(), name='login'),
    path('auth/register/', RegisterView.as_view(), name='register'),
    path('auth/logout/', LogoutView.as_view(next_page='/'), name='logout'),
    
    # Account Recovery
    path('auth/recover/', PasswordResetView.as_view(template_name='users/recover/password-reset.html'), name='password_reset'),
    path('auth/recover/done/', PasswordResetDoneView.as_view(template_name='users/recover/password-reset-done.html'), name='password_reset_done'),
    path('auth/recover/confirm/<uidb64>/<slug:token>/', PasswordResetConfirmView.as_view(template_name='users/recover/password-reset-confirm.html'), name='password_reset_confirm'),
    path('auth/recover/complete/', PasswordResetCompleteView.as_view(template_name='users/recover/password-reset-complete.html'), name='password_reset_complete'),

    # TODO: Add settings pages
    #path('settings/', SettingsView.as_view(), name='settings'),
    #path('settings/purchases/', PurchasesView.as_view(), name='purchases'),

    path('newsletter/subscribe/', NewsletterSubscribeView.as_view(), name='newsletter_subscribe'),
    path('newsletter/unsubscribe/', NewsletterUnSubscribeView.as_view(), name='newsletter_unsubscribe'),
    path('newsletter/subscribed/', TemplateView.as_view(template_name='newsletter/subscribed.html'), name='newsletter_subscribed'),
    path('newsletter/unsubscribed/', TemplateView.as_view(template_name='newsletter/unsubscribed.html'), name='newsletter_unsubscribed'),

    path('admin/', admin.site.urls),
    path('dev/', TemplateView.as_view(template_name='developer.html')),

    # TODO: TOS and PP as TemplateView
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


admin.site.site_header = 'Chain Gang Entertainment Inc AdminCP'
admin.site.site_title = 'Chain Gang Entertainment Inc AdminCP'

# admin.site.__class__ = OTPAdminSite