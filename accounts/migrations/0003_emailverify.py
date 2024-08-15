# Generated by Django 5.1 on 2024-08-15 08:55

import datetime
import django_jalali.db.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0002_alter_users_mobile_phone"),
    ]

    operations = [
        migrations.CreateModel(
            name="EmailVerify",
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
                (
                    "email",
                    models.EmailField(
                        max_length=254, unique=True, verbose_name="email address"
                    ),
                ),
                ("code", models.PositiveIntegerField(blank=True, null=True)),
                (
                    "expired_code",
                    django_jalali.db.models.jDateTimeField(
                        blank=True,
                        default=datetime.timedelta(seconds=120),
                        null=True,
                        verbose_name="expired code",
                    ),
                ),
            ],
            options={
                "verbose_name": "email verify",
                "verbose_name_plural": "email verify",
                "db_table": "email_verify",
            },
        ),
    ]
