"""boutique_ado URL Configuration"""
from .views import handler404
import os
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views.static import serve

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('home.urls')),
    path('products/', include('products.urls')),
    path('bag/', include('bag.urls')),
    path('checkout/', include('checkout.urls')),
    path('profile/', include('profiles.urls')),
    path('wishlist/', include('wishlist.urls')),
]

if os.getenv("USE_AWS") == "True":
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
else:
    urlpatterns += [
        path("media/<path:path>", serve, {"document_root": settings.MEDIA_ROOT}),
    ]

handler404 = 'boutique_ado.views.handler404'
