from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

from products.filters import ProductFilter
from products.models import Category, Review
from products.serialziers import Product, ProductSerialize, CategorySerializer, ReviewSerializer
from products.pagination import DefaultPagination
from products.permissions import IsOwnerOrReadOnly


class ProductViewSet(ReadOnlyModelViewSet):
    queryset = Product.objects.select_related('category', 'image').filter(is_active=True)
    serializer_class = ProductSerialize
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = ProductFilter
    search_fields = ['title']
    ordering_fields = ['is_available', 'price', 'update_at']
    pagination_class = DefaultPagination

    # def retrieve(self, request, *args, **kwargs):
    #     pk = self.kwargs.get('pk')
    #     slug = self.kwargs.get('en_slug')
    #     instance = get_object_or_404(self.get_queryset(), pk=pk, en_slug=slug)
    #     serializer = self.get_serializer(instance)
    #     return Response(serializer.data)


class CategoryViewSet(ReadOnlyModelViewSet):
    queryset = Category.objects.select_related('parent').all()
    serializer_class = CategorySerializer


class ReviewViewSet(ModelViewSet):
    serializer_class = ReviewSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user, product_id=self.kwargs['product_pk'])

    def get_serializer_context(self):
        return {'product_id': self.kwargs['product_pk']}

    def get_queryset(self):
        return (Review.objects.filter(product_id=self.kwargs['product_pk'], is_active=True, user__is_active=True).
                select_related('user', 'product'))
