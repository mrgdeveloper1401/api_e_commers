from django.urls import include
from rest_framework.urls import path
from products.views import ProductViewSet, CategoryViewSet, ReviewViewSet
from rest_framework_nested import routers


app_name = 'products'
router = routers.DefaultRouter()
router.register('category', CategoryViewSet, basename='category')
router.register('product', ProductViewSet, basename='products')

product_router = routers.NestedDefaultRouter(router, 'product', lookup='product')
product_router.register('reviews', ReviewViewSet, basename='review')

urlpatterns = [
    path('', include(router.urls), name='category'),
    path('', include(product_router.urls), name='products'),
    # path('product/<int:pk>/<slug:en_slug>/', ProductViewSet.as_view({'get': 'retrieve'}), name='product_detail'),
]
urlpatterns += router.urls + product_router.urls
