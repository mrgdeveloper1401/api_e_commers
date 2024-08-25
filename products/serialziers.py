from rest_framework.generics import get_object_or_404
from rest_framework.serializers import ModelSerializer, HyperlinkedRelatedField, CharField, SerializerMethodField

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

    class Meta:
        model = Product
        fields = ['category', 'manufacturer', 'fa_title', 'en_title', 'fa_slug', 'en_slug', 'description', 'price',
                  'calc_value_price', 'calc_percent_price', 'calculate_tax', 'image', 'is_available']

        extra_kwargs = {
            'en_slug': {'write_only': True},
            'fa_slug': {'write_only': True},
        }


class ReviewSerializer(ModelSerializer):
    user = CharField(read_only=True)
    product = CharField(read_only=True)

    class Meta:
        model = Review
        fields = ['user', 'product', 'title', 'review_body', 'rate']

    def create(self, validated_data):
        return Review.objects.create(**validated_data)

    def validate(self, attrs):
        product_id = self.context['product_id']
        product = get_object_or_404(Product, pk=product_id)
        if product:
            return attrs
