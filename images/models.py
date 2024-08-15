from hashlib import sha1
from django.db import models
from django.utils.translation import gettext_lazy as _
from core.models import UpdateMixin, CreateMixin, SoftDeleteMixin


# Create your models here.
class Image(CreateMixin, UpdateMixin, SoftDeleteMixin):
    image = models.ImageField(upload_to='%Y/%m/%d', width_field='image_width', height_field='image_height')
    image_width = models.PositiveIntegerField(default=0)
    image_height = models.PositiveIntegerField(default=0)
    image_hash = models.CharField(max_length=255, blank=True, null=True)
    image_alt_text = models.CharField(max_length=255, blank=True, null=True)
    image_size = models.PositiveIntegerField(default=0)
    image_file_name = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.image_hash

    def generate_image_hash(self):
        hasher = sha1()
        for c in self.image.chunks():
            hasher.update(c)
        return hasher.hexdigest()

    def save(self, *args, **kwargs):
        self.image_hash = self.generate_image_hash()
        self.image_size = self.image.size
        return super().save(*args, **kwargs)

    class Meta:
        db_table = 'images'