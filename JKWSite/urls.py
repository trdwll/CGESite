from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

import debug_toolbar

from machina.app import board

from . import views
from users.views import LoginView, RegisterView

handler404 = views.handler404
handler500 = views.handler500


urlpatterns = [
    path('', views.HomeView.as_view(), name='home_page'),

    path('forum/', include(board.urls)),
    path('store/', include('store.urls')),

    path('auth/login/', LoginView.as_view(), name='login'),
    path('auth/register/', RegisterView.as_view(), name='register'),
    #path('auth/recover/', RecoverView.as_view(), name='user_recover_page'),
    #path('auth/recover/step2/', RecoverTokenView.as_view(), name='user_token_page'),

    path('auth/', include('social_django.urls', namespace='social')),

    path('admin/', admin.site.urls),

    path('__debug__/', include(debug_toolbar.urls)),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


admin.site.site_header = 'JKW Productions Inc AdminCP'
admin.site.site_title = 'JKW Productions Inc AdminCP'

# admin.site.__class__ = OTPAdminSite