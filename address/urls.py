from django.urls import include
from rest_framework.urls import path
from rest_framework.routers import DefaultRouter
from address.views import AddressViewSet


app_name = 'address'
router = DefaultRouter()
router.register('profile_address', AddressViewSet, basename='address')

urlpatterns = [
    path('', include(router.urls)),
]
