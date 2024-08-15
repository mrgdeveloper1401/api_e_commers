from django.dispatch.dispatcher import receiver
from django.db.models.signals import post_save
from inventory.models import PersonalShop, ProfileShop


@receiver(post_save, sender=PersonalShop)
def create_profile_inventory(sender, instance, created, **kwargs):
    if created:
        profile = ProfileShop.objects.create(identity_inventory=instance)
        profile.save()
