from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from accounts.models import Users
from orders.models import Cart, CartItem
from products.models import Product


class SimpleProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ['title', 'price']


class SimpleUserSerializer(ModelSerializer):
    class Meta:
        model = Users
        fields = ['username']


class UpdateCartItemSerializer(ModelSerializer):
    class Meta:
        model = CartItem
        fields = ['quantity']


class CartItemSerializer(ModelSerializer):
    product = SimpleProductSerializer()
    total_product_price = serializers.SerializerMethodField(method_name='get_total_price')

    def get_total_price(self, cart_item: CartItem):
        return cart_item.product.price * cart_item.quantity

    class Meta:
        model = CartItem
        fields = ['product', 'quantity', 'total_product_price']


class CartsSerializer(ModelSerializer):
    cart_item = CartItemSerializer(many=True, read_only=True)
    total_price = serializers.SerializerMethodField(method_name='get_total_price')
    user = SimpleUserSerializer()

    class Meta:
        model = Cart
        fields = ['user', 'id', 'cart_item', "total_price"]

    def get_total_price(self, cart: Cart):
        res = [item.product.price * item.quantity for item in cart.cart_item.all()]
        return sum(res)


class AddCartItemSerialize(ModelSerializer):
    product_id = serializers.IntegerField()
    
    def save(self, **kwargs):
        cart_id = self.context['cart_id']
        product_id = self.validated_data['product_id']
        quantity = self.validated_data['quantity']

        try:
            cart_item = CartItem.objects.get(cart_id=cart_id, product_id=product_id)
            cart_item.quantity += quantity
            cart_item.save()
            self.instance = cart_item
        except CartItem.DoesNotExist:
            self.instance = CartItem.objects.create(cart_id=cart_id, **self.validated_data)
        return self.instance

    def validate_product_id(self, value):
        if not Product.objects.filter(pk=value).exists():
            raise serializers.ValidationError('product not found')
        return value

    class Meta:
        model = CartItem
        fields = ['product_id', 'quantity']

