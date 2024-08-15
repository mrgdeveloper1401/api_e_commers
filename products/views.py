from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from products.filters import ProductFilter
from products.models import Category, Review
from products.serialziers import Product, ProductSerialize, CategorySerializer, ReviewSerializer
from products.pagination import DefaultPagination


class ProductViewSet(ReadOnlyModelViewSet):
    queryset = Product.objects.select_related('category', 'image').filter(is_active=True)
    serializer_class = ProductSerialize
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = ProductFilter
    search_fields = ['title']
    ordering_fields = ['is_available', 'price', 'update_at']
    pagination_class = DefaultPagination


class CategoryViewSet(ReadOnlyModelViewSet):
    queryset = Category.objects.select_related('parent').all()
    serializer_class = CategorySerializer


class ReviewViewSet(ModelViewSet):
    serializer_class = ReviewSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_serializer_context(self):
        return {'product_id': self.kwargs['product_pk'],
                'request': self.request}

    def get_queryset(self):
        return Review.objects.filter(product_id=self.kwargs['product_pk'], is_active=True).select_related('user')

    def get_permissions(self):
        if self.request.method == 'get':
            return [AllowAny()]
        return super().get_permissions()
