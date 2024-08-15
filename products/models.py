from decimal import Decimal

from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _
from core.models import UpdateMixin, CreateMixin, SoftDeleteMixin
from django_jalali.db.models import jDateTimeField, jDateField
from django.core.validators import MinValueValidator


# Create your models here.
class Category(CreateMixin, UpdateMixin):
    title = models.CharField(max_length=255)
    parent = models.ForeignKey('self', on_delete=models.PROTECT, related_name='children',
                               blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'category'
        verbose_name_plural = _('categories')


class Promotion(CreateMixin, UpdateMixin, SoftDeleteMixin):
    pass


class Product(CreateMixin, UpdateMixin, SoftDeleteMixin):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, allow_unicode=True)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=12, decimal_places=3, validators=[MinValueValidator(Decimal(0))])
    image = models.ForeignKey('images.Image', on_delete=models.PROTECT, related_name='image_product')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='category_product')
    is_available = models.BooleanField(default=True)
    views = models.PositiveIntegerField(default=0)
    sales = models.PositiveIntegerField(default=0)
    last_viewed_at = jDateTimeField(blank=True, null=True)
    last_purchased_at = jDateTimeField(blank=True, null=True)
    discount_percent = models.PositiveIntegerField(default=0)
    discount_value = models.DecimalField(max_digits=12, decimal_places=3, validators=[MinValueValidator(Decimal(0))],
                                         default=0)
    manufacturer = models.ForeignKey("ManyFacture", on_delete=models.PROTECT, related_name='manufacturer_product')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    def calculate_tax(self):
        return self.price * Decimal(0.1)

    def review_count(self):
        return self.reviews.count()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    class Meta:
        db_table = 'products'


class ManyFacture(CreateMixin, UpdateMixin, SoftDeleteMixin):
    manufacturer_name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.manufacturer_name

    class Meta:
        db_table = 'many_facture'
        verbose_name_plural = _('many_facture')


class Warranty(CreateMixin, UpdateMixin, SoftDeleteMixin):
    product = models.OneToOneField(Product, on_delete=models.PROTECT, related_name='warranty_product')
    duration = models.PositiveIntegerField(default=12)
    provider = models.CharField(max_length=100)
    terms = models.TextField()
    start_date = jDateField()
    end_date = jDateField()
    contract_info = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.product.title} {self.provider}"

    class Meta:
        db_table = 'warranty'
        verbose_name_plural = _('warranties')


class ProductAttribute(CreateMixin, UpdateMixin, SoftDeleteMixin):
    attribute = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.attribute

    class Meta:
        db_table = 'product_attribute'
        verbose_name_plural = _('product attributes')


class ProductAttributeValue(CreateMixin, UpdateMixin, SoftDeleteMixin):
    product = models.ForeignKey(Product, on_delete=models.PROTECT, related_name='product_attribute_value')
    attribute = models.ForeignKey(ProductAttribute, on_delete=models.PROTECT, related_name='attribute_value')
    char_value = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.attribute} {self.char_value}'

    class Meta:
        db_table = 'product_attribute_value'
        verbose_name_plural = _('product attribute values')


class Review(CreateMixin, UpdateMixin, SoftDeleteMixin):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey('accounts.Users', on_delete=models.CASCADE, related_name='user_reviews')
    title = models.CharField(max_length=255)
    review_body = models.TextField()
    is_active = models.BooleanField(default=True)

    class ProductRateChoices(models.TextChoices):
        one = 'one'
        two = 'two'
        three = 'three'
        four = 'four'
        five = 'five'
    rate = models.CharField(max_length=5, choices=ProductRateChoices.choices, blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'reviews'
        verbose_name_plural = _('reviews')