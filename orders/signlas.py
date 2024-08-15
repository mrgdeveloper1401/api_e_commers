from django.db.models.signals import post_save
from django.dispatch.dispatcher import receiver

from orders.models import Cart
from accounts.models import Users


@receiver(post_save, sender=Users)
def create_cart(sender, instance, created, **kwargs):
    if created:
        cart = Cart.objects.create(user=instance)
        cart.save()
