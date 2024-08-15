# Generated by Django 5.1 on 2024-08-14 08:40

import django_jalali.db.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Image",
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
                (
                    "image",
                    models.ImageField(
                        height_field="image_height",
                        upload_to="%Y/%m/%d",
                        width_field="image_width",
                    ),
                ),
                ("image_width", models.PositiveIntegerField(default=0)),
                ("image_height", models.PositiveIntegerField(default=0)),
                ("image_hash", models.CharField(blank=True, max_length=255, null=True)),
                (
                    "image_alt_text",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                ("image_size", models.PositiveIntegerField(default=0)),
                (
                    "image_file_name",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
            ],
            options={
                "db_table": "images",
            },
        ),
    ]
