from django_filters.rest_framework import FilterSet

from products.models import Product


class ProductFilter(FilterSet):
    class Meta:
        model = Product
        fields = {
            'price': ['range', 'lte', 'gte'],
            # 'title': ['contains'],
            'category': ['exact'],
            "manufacturer": ['exact']
        }
