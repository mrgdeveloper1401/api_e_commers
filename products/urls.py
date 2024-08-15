from django.urls import include
from rest_framework.urls import path
from products.views import ProductViewSet, CategoryViewSet, ReviewViewSet
from rest_framework_nested import routers


app_name = 'products'
router = routers.DefaultRouter()
router.register('category', CategoryViewSet, basename='category')
router.register('product', ProductViewSet, basename='products')

product_router = routers.NestedDefaultRouter(router, 'product', lookup='product')
product_router.register('reviews', ReviewViewSet, basename='product_reviews')

urlpatterns = [
    path('', include(router.urls), name='category'),
    path('', include(router.urls), name='products'),
]
urlpatterns += router.urls + product_router.urls
