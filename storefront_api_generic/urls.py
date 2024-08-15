"""
URL configuration for storefront_api_generic project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from debug_toolbar.toolbar import debug_toolbar_urls
from django.conf.urls.static import static
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

accounts_api = [
    path('user/', include('accounts.urls', namespace='accounts')),
]

product_api = [
    path('', include('products.urls', namespace='products')),
]

image_api = [
    path('', include('images.urls', namespace='image'))
]

address_urls = [
    path('address/', include('address.urls', namespace='address')),
]

orders_urls = [
    path('', include('orders.urls', namespace='orders')),
]

inventory_urls = [
    path('', include('inventory.urls', namespace='inventory'))
]

urlpatterns = [
    path('admin/', admin.site.urls),
    # YOUR PATTERNS
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    # Optional UI:
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # djoser
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),

] + debug_toolbar_urls()

urlpatterns += accounts_api + product_api + image_api + orders_urls + address_urls + inventory_urls

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
