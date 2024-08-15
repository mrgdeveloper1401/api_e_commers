from django.db import models
from django.utils.translation import gettext_lazy as _
from core.models import UpdateMixin, CreateMixin, SoftDeleteMixin


# Create your models here.
class Address(CreateMixin, UpdateMixin, SoftDeleteMixin):
    user = models.ForeignKey('accounts.Users', on_delete=models.PROTECT, related_name='user_address')
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    street = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=15, unique=True)
    description_address = models.TextField(blank=True, null=True,
                                           help_text=_('give more details about address'))
    is_active = models.BooleanField(default=True)
    is_default_address = models.BooleanField(default=True)

    class Meta:
        db_table = 'address'
        verbose_name_plural = _('address')


class OtherCustomer(CreateMixin, UpdateMixin, SoftDeleteMixin):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=15)
    address = models.ForeignKey(Address, on_delete=models.PROTECT, related_name='address_customer')

    class Meta:
        db_table = 'other_customer'
        verbose_name_plural = _('other customers')
