from django.dispatch.dispatcher import receiver
from django.db.models.signals import post_save
from jdatetime import datetime, timedelta

from accounts.models import Users, MobileVerify
from storefront_api_generic.generate_random_code import random_code


@receiver(post_save, sender=Users)
def create_code(sender, instance, created, **kwargs):
    if created:
        MobileVerify.objects.create(
            mobile_phone=instance.mobile_phone,
            code=random_code(),
            expired_code=datetime.now() + timedelta(minutes=2))
