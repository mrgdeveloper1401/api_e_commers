from rest_framework.mixins import DestroyModelMixin, RetrieveModelMixin, ListModelMixin, UpdateModelMixin, CreateModelMixin
from rest_framework.viewsets import GenericViewSet
from django.db.models import Prefetch
from orders.serializers import CartsSerializer, CartItemSerializer, UpdateCartItemSerializer, AddCartItemSerialize
from orders.models import Cart, CartItem
from products.models import Product


# Create your views here.
class CartsViewSet(RetrieveModelMixin, GenericViewSet):
    queryset = Cart.objects.prefetch_related(
        Prefetch('cart_item', CartItem.objects.select_related('product'))
    )
    serializer_class = CartsSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CartItemViewSet(ListModelMixin, CreateModelMixin, RetrieveModelMixin, DestroyModelMixin, UpdateModelMixin, GenericViewSet):
    http_method_names = ['get', 'post', 'patch', 'delete']
    queryset = CartItem.objects.select_related('product')
    serializer_class = CartItemSerializer

    def get_serializer_class(self):
        if self.request.method == 'PATCH':
            return UpdateCartItemSerializer
        elif self.request.method == 'POST':
            return AddCartItemSerialize
        return super().get_serializer_class()
    
    def get_serializer_context(self):
        return {'cart_id': self.kwargs['cart_pk']}
