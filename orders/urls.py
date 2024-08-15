from django.urls import include
from rest_framework.urls import path
from rest_framework_nested.routers import DefaultRouter, NestedDefaultRouter
from orders.views import CartsViewSet, CartItemViewSet


router = DefaultRouter()
router.register('cart', CartsViewSet, basename='cart')

cart_router = NestedDefaultRouter(router, 'cart', lookup='cart')
cart_router.register('cart_item', CartItemViewSet, basename='cart_item')

app_name = 'orders'

urlpatterns = [
    path('', include(router.urls)),
    path('', include(cart_router.urls)),
]
