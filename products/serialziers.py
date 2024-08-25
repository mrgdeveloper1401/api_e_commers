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
        fields = ['category', 'manufacturer', 'fa_title', 'en_title', 'fa_slug', 'en_slug', 'description', 'price',
                  'calc_value_price', 'calc_percent_price', 'tax', 'image', 'is_available']

        extra_kwargs = {
            'en_slug': {'write_only': True},
            'fa_slug': {'write_only': True},
        }

    def calculate_tax(self, product: Product):
        return product.calculate_tax()


class ReviewSerializer(ModelSerializer):
    user = CharField(read_only=True)
    product = CharField(read_only=True)

    class Meta:
        model = Review
        fields = ['user', 'product', 'title', 'review_body', 'rate']

    def create(self, validated_data):
        return Review.objects.create(**validated_data)
