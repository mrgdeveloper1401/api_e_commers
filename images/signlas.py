from django.db.models.signals import post_save
from django.dispatch.dispatcher import receiver

from images.models import Image


@receiver(post_save, sender=Image)
def read_filename(sender, instance, created, **kwargs):
    if created:
        image_filename = Image.objects.get(pk=instance.id)
        read = image_filename.image.name
        image_filename.image_file_name = read
        image_filename.save()
