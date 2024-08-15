from django.contrib.auth.models import UserManager
from django.db import models


class PublishModel(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)