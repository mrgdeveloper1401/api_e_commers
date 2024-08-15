from uuid import uuid4
from django.db import models
from core.models import CreateMixin, UpdateMixin, SoftDeleteMixin
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator


# Create your models here.
class Cart(CreateMixin):
    id = models.UUIDField(default=uuid4, editable=False, primary_key=True)
    user = models.ForeignKey('accounts.Users', on_delete=models.CASCADE, related_name='user_cart',
                             blank=True, null=True)
    cart_complete = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.create_at.strftime("%d/%m/%Y %H:%M")} {self.user}'

    class Meta:
        db_table = 'cart'


class CartItem(CreateMixin, UpdateMixin):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='cart_item')
    user = models.ForeignKey('accounts.Users', on_delete=models.CASCADE, related_name='user_cart_item',
                             blank=True, null=True)
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE, related_name='cart_item_product')
    quantity = models.PositiveIntegerField(default=1,
                                           validators=[MinValueValidator(1)])

    def __str__(self):
        return f"{self.quantity} {self.product}"

    class Meta:
        db_table = 'cart_item'
        unique_together = [('cart', 'product'), ]


class Order(SoftDeleteMixin, CreateMixin, UpdateMixin):
    user = models.ForeignKey('accounts.Users', on_delete=models.CASCADE, related_name='user_order')
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE, related_name='order_product')

    class StatusChoices(models.TextChoices):
        pending = 'pending'
        completed = 'completed'
        failed = 'failed'

    status = models.CharField(max_length=9, choices=StatusChoices.choices, default=StatusChoices.pending)

    def __str__(self):
        return f"{self.user.get_full_name()} {self.product} {self.status}"

    class Meta:
        db_table = 'order'
        permissions = [
            ('cancel_order', 'Can cancel order'),
        ]


class OrderItem(CreateMixin, UpdateMixin, SoftDeleteMixin):
    order = models.ForeignKey(Order, on_delete=models.PROTECT, related_name='order_item')
    is_canceled = models.BooleanField(default=False)
    reason_canceled = models.TextField(blank=True, null=True,
                                       help_text=_('if order is cancel you explain why this order is canceled'))

    class Meta:
        db_table = 'order_item'
        verbose_name_plural = _('order items')
