# Generated by Django 5.1 on 2024-08-14 08:40

import django.db.models.deletion
import django_jalali.db.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Address",
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
                ("state", models.CharField(max_length=50)),
                ("city", models.CharField(max_length=50)),
                ("street", models.CharField(max_length=50)),
                ("postal_code", models.CharField(max_length=15, unique=True)),
                (
                    "description_address",
                    models.TextField(
                        blank=True,
                        help_text="give more details about address",
                        null=True,
                    ),
                ),
                ("is_active", models.BooleanField(default=True)),
                ("is_default_address", models.BooleanField(default=True)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="user_address",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "address",
                "db_table": "address",
            },
        ),
        migrations.CreateModel(
            name="OtherCustomer",
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
                ("first_name", models.CharField(max_length=100)),
                ("last_name", models.CharField(max_length=100)),
                ("mobile_number", models.CharField(max_length=15)),
                (
                    "address",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="address_customer",
                        to="address.address",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "other customers",
                "db_table": "other_customer",
            },
        ),
    ]
