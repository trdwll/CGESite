from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView


from . import views

handler404 = views.handler404
handler500 = views.handler500


urlpatterns = [
    path('admin/', admin.site.urls),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


admin.site.site_header = 'JKW Productions Inc AdminCP'
admin.site.site_title = 'JKW Productions Inc AdminCP'

# admin.site.__class__ = OTPAdminSite