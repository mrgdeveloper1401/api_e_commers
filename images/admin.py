from django.contrib import admin
from images.models import Image


# Register your models here.
@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['image_width', 'image_height', "image_size", 'image_file_name']
