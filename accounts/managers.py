from django.contrib.auth.models import BaseUserManager
from django.db import models


class PublishModel(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)


class UserManager(BaseUserManager):
    def _create_user(self, mobile_phone, password=None, **extra_fields):
        if not mobile_phone:
            raise ValueError('Mobile phone is required')
        user = self.model(mobile_phone=mobile_phone, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, mobile_phone, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(mobile_phone, password, **extra_fields)

    def create_superuser(self, mobile_phone, first_name, last_name, password=None):
        if not first_name:
            raise ValueError('First name is required')
        if not last_name:
            raise ValueError('Last name is required')
        user = self.model(mobile_phone=mobile_phone, first_name=first_name, last_name=last_name)
        user.set_password(password)
        user.is_staff = True
        user.is_superuser = True
        user.is_active = True
        user.verify_account = True
        user.save(using=self._db)
        return user

