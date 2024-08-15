from django.db import models
from django_jalali.db.models import jDateTimeField


# Create your models here.
class CreateMixin(models.Model):
    create_at = jDateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class UpdateMixin(models.Model):
    update_at = jDateTimeField(auto_now=True)

    class Meta:
        abstract = True


class SoftDeleteMixin(models.Model):
    deleted_at = jDateTimeField(blank=True, null=True, editable=False)
    is_deleted = models.BooleanField(default=False, editable=False)

    class Meta:
        abstract = True
