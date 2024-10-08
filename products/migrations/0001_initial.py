# Generated by Django 5.1 on 2024-08-24 17:03

import django.core.validators
import django.db.models.deletion
import django_jalali.db.models
from decimal import Decimal
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("images", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="ManyFacture",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "create_at",
                    django_jalali.db.models.jDateTimeField(auto_now_add=True),
                ),
                ("update_at", django_jalali.db.models.jDateTimeField(auto_now=True)),
                (
                    "deleted_at",
                    django_jalali.db.models.jDateTimeField(
                        blank=True, editable=False, null=True
                    ),
                ),
                ("is_deleted", models.BooleanField(default=False, editable=False)),
                ("manufacturer_name", models.CharField(max_length=100)),
                ("is_active", models.BooleanField(default=True)),
            ],
            options={
                "verbose_name_plural": "many_facture",
                "db_table": "many_facture",
            },
        ),
        migrations.CreateModel(
            name="ProductAttribute",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "create_at",
                    django_jalali.db.models.jDateTimeField(auto_now_add=True),
                ),
                ("update_at", django_jalali.db.models.jDateTimeField(auto_now=True)),
                (
                    "deleted_at",
                    django_jalali.db.models.jDateTimeField(
                        blank=True, editable=False, null=True
                    ),
                ),
                ("is_deleted", models.BooleanField(default=False, editable=False)),
                ("attribute", models.CharField(max_length=255, unique=True)),
            ],
            options={
                "verbose_name_plural": "product attributes",
                "db_table": "product_attribute",
            },
        ),
        migrations.CreateModel(
            name="Promotion",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "create_at",
                    django_jalali.db.models.jDateTimeField(auto_now_add=True),
                ),
                ("update_at", django_jalali.db.models.jDateTimeField(auto_now=True)),
                (
                    "deleted_at",
                    django_jalali.db.models.jDateTimeField(
                        blank=True, editable=False, null=True
                    ),
                ),
                ("is_deleted", models.BooleanField(default=False, editable=False)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "create_at",
                    django_jalali.db.models.jDateTimeField(auto_now_add=True),
                ),
                ("update_at", django_jalali.db.models.jDateTimeField(auto_now=True)),
                ("title", models.CharField(max_length=255)),
                (
                    "parent",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="children",
                        to="products.category",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "categories",
                "db_table": "category",
            },
        ),
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "create_at",
                    django_jalali.db.models.jDateTimeField(auto_now_add=True),
                ),
                ("update_at", django_jalali.db.models.jDateTimeField(auto_now=True)),
                (
                    "deleted_at",
                    django_jalali.db.models.jDateTimeField(
                        blank=True, editable=False, null=True
                    ),
                ),
                ("is_deleted", models.BooleanField(default=False, editable=False)),
                ("fa_title", models.CharField(max_length=255)),
                ("en_title", models.CharField(max_length=255)),
                (
                    "fa_slug",
                    models.SlugField(allow_unicode=True, max_length=255, unique=True),
                ),
                ("en_slug", models.SlugField(max_length=255, unique=True)),
                ("description", models.TextField(blank=True, null=True)),
                (
                    "price",
                    models.DecimalField(
                        decimal_places=3,
                        max_digits=12,
                        validators=[
                            django.core.validators.MinValueValidator(Decimal("0"))
                        ],
                    ),
                ),
                ("is_available", models.BooleanField(default=True)),
                ("views", models.PositiveIntegerField(default=0)),
                ("sales", models.PositiveIntegerField(default=0)),
                (
                    "last_viewed_at",
                    django_jalali.db.models.jDateTimeField(blank=True, null=True),
                ),
                (
                    "last_purchased_at",
                    django_jalali.db.models.jDateTimeField(blank=True, null=True),
                ),
                ("discount_percent", models.PositiveIntegerField(default=0)),
                (
                    "discount_value",
                    models.DecimalField(
                        decimal_places=3,
                        default=0,
                        max_digits=12,
                        validators=[
                            django.core.validators.MinValueValidator(Decimal("0"))
                        ],
                    ),
                ),
                ("is_active", models.BooleanField(default=True)),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="category_product",
                        to="products.category",
                    ),
                ),
                (
                    "image",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="image_product",
                        to="images.image",
                    ),
                ),
                (
                    "manufacturer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="manufacturer_product",
                        to="products.manyfacture",
                    ),
                ),
            ],
            options={
                "db_table": "products",
            },
        ),
        migrations.CreateModel(
            name="ProductAttributeValue",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "create_at",
                    django_jalali.db.models.jDateTimeField(auto_now_add=True),
                ),
                ("update_at", django_jalali.db.models.jDateTimeField(auto_now=True)),
                (
                    "deleted_at",
                    django_jalali.db.models.jDateTimeField(
                        blank=True, editable=False, null=True
                    ),
                ),
                ("is_deleted", models.BooleanField(default=False, editable=False)),
                ("char_value", models.CharField(max_length=100)),
                (
                    "attribute",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="attribute_value",
                        to="products.productattribute",
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="product_attribute_value",
                        to="products.product",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "product attribute values",
                "db_table": "product_attribute_value",
            },
        ),
        migrations.CreateModel(
            name="Review",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "create_at",
                    django_jalali.db.models.jDateTimeField(auto_now_add=True),
                ),
                ("update_at", django_jalali.db.models.jDateTimeField(auto_now=True)),
                (
                    "deleted_at",
                    django_jalali.db.models.jDateTimeField(
                        blank=True, editable=False, null=True
                    ),
                ),
                ("is_deleted", models.BooleanField(default=False, editable=False)),
                ("title", models.CharField(max_length=255)),
                ("review_body", models.TextField()),
                ("is_active", models.BooleanField(default=True)),
                (
                    "rate",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("one", "One"),
                            ("two", "Two"),
                            ("three", "Three"),
                            ("four", "Four"),
                            ("five", "Five"),
                        ],
                        max_length=5,
                        null=True,
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="reviews",
                        to="products.product",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="user_reviews",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "reviews",
                "db_table": "reviews",
            },
        ),
        migrations.CreateModel(
            name="Warranty",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "create_at",
                    django_jalali.db.models.jDateTimeField(auto_now_add=True),
                ),
                ("update_at", django_jalali.db.models.jDateTimeField(auto_now=True)),
                (
                    "deleted_at",
                    django_jalali.db.models.jDateTimeField(
                        blank=True, editable=False, null=True
                    ),
                ),
                ("is_deleted", models.BooleanField(default=False, editable=False)),
                ("duration", models.PositiveIntegerField(default=12)),
                ("provider", models.CharField(max_length=100)),
                ("terms", models.TextField()),
                ("start_date", django_jalali.db.models.jDateField()),
                ("end_date", django_jalali.db.models.jDateField()),
                ("contract_info", models.CharField(max_length=15)),
                (
                    "product",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="warranty_product",
                        to="products.product",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "warranties",
                "db_table": "warranty",
            },
        ),
    ]
