from django.db import models
from core.models import CreateMixin, UpdateMixin, SoftDeleteMixin
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey


# Create your models here.
class Tag(CreateMixin, UpdateMixin, SoftDeleteMixin):
    user = models.ForeignKey('accounts.Users', on_delete=models.CASCADE,
                             related_name='user_tag',
                             blank=True,
                             null=True)
    tag_name = models.CharField(max_length=100, unique=True)
    is_active = models.BooleanField(default=True)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    
    class Meta:
        db_table = 'tag'
