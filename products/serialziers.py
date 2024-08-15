from rest_framework.serializers import ModelSerializer, HyperlinkedRelatedField, CharField, SerializerMethodField, \
    URLField

from accounts.models import Users
from images.models import Image
from products.models import Product, Category, Review, ManyFacture


class CategorySerializer(ModelSerializer):
    parent = CharField()

    class Meta:
        model = Category
        fields = ['title', 'parent']


class BrandSerializer(ModelSerializer):
    class Meta:
        model = ManyFacture
        fields = ['manufacturer_name']


class ProductSerialize(ModelSerializer):
    category = CategorySerializer()
    manufacturer = BrandSerializer()
    image = HyperlinkedRelatedField(view_name='image:details_image',
                                    queryset=Image.objects.all())
    tax = SerializerMethodField(method_name='calculate_tax')

    class Meta:
        model = Product
        fields = ['category', 'manufacturer', 'title', 'slug', 'description', 'price', 'tax', 'image', 'is_available']

        extra_kwargs = {
            'slug': {'write_only': True},
        }

    def calculate_tax(self, product: Product):
        return product.calculate_tax()


class ReviewSerializer(ModelSerializer):
    user = HyperlinkedRelatedField(view_name="accounts:profile",
                                   queryset=Users.objects.all())

    class Meta:
        model = Review
        fields = ['user', 'title', 'review_body', 'rate']

    def create(self, validated_data):
        product_id = self.context['product_id']
        return Review.objects.create(product_id=product_id, **validated_data)
