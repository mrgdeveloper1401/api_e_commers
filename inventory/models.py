from django.db import models
from core.models import CreateMixin, UpdateMixin, SoftDeleteMixin
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator
# Create your models here.


class PersonalShop(CreateMixin, UpdateMixin, SoftDeleteMixin):
    first_name = models.CharField(_('First Name'), max_length=50)
    last_name = models.CharField(_('Last Name'), max_length=50)
    nation_code = models.CharField(_('National Code'), max_length=15, unique=True)
    mobile_phone = models.CharField(_('Mobile Phone'), max_length=15, unique=True)
    email = models.EmailField(_('Email'), unique=True)
    is_legal = models.BooleanField(_('Is Legal'), default=False,
                                   help_text=_("Check this box if you are a legal entity"))
    is_active = models.BooleanField(_('Is Active'), default=False)

    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.nation_code}'

    class Meta:
        db_table = 'personal_shop'
        verbose_name = _('personal shop')
        verbose_name_plural = _('personal shop')


class ProfileShop(CreateMixin, UpdateMixin, SoftDeleteMixin):
    identity_inventory = models.OneToOneField(PersonalShop, on_delete=models.PROTECT,
                                              related_name="profile_inventory")
    is_active = models.BooleanField(_('Is Active'), default=False)
    is_verify = models.BooleanField(_('Is Verify'), default=False)
    image = models.ForeignKey("images.Image", on_delete=models.PROTECT, related_name='image_inventory',
                              blank=True, null=True)
    bio = models.TextField(_('Bio'), blank=True, null=True)
    company_name = models.CharField(_('Company Name'), max_length=50, blank=True, null=True)
    economy_code = models.CharField(_('Economy Code'), max_length=15, blank=True, null=True)
    certificate = models.ForeignKey("CertificateShop", on_delete=models.PROTECT,
                                    related_name='certificate_inventory', blank=True, null=True)
    level_type_of_activity = models.TextField(_('Type of Activity'), blank=True, null=True)
    company_date_registration = models.DateField(_('Company Registration Date'), blank=True, null=True)
    sheba_number = models.CharField(_('Sheba Number or cart number'), max_length=24, blank=True, null=True)
    is_complete_profile = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.identity_inventory}'

    class Meta:
        db_table = 'profile_shop'
        verbose_name = _('Profile shop')
        verbose_name_plural = _('Profile shop')


class CertificateShop(CreateMixin, UpdateMixin, SoftDeleteMixin):
    image = models.ForeignKey("images.Image", on_delete=models.PROTECT, related_name='image_certificate_inventory')
    is_active_image = models.BooleanField(_('Is Active'), default=True)

    class Meta:
        db_table = 'certificate_shop'
        verbose_name = _('Certificate shop')
        verbose_name_plural = _('Certificate shop')


class RecordProduct(CreateMixin, UpdateMixin, SoftDeleteMixin):
    product = models.ForeignKey('products.Product', on_delete=models.PROTECT, related_name="profile_record_product")
    profile_inventory = models.ForeignKey(ProfileShop, on_delete=models.PROTECT,
                                          related_name="profile_record_product")
    product_amount = models.PositiveSmallIntegerField(default=1, validators=[MinValueValidator(1)])
    is_delivery = models.BooleanField(_('Is Delivery'), default=True)

    def __str__(self):
        return f"{self.product} {self.profile_inventory}"

    class Meta:
        db_table = 'record_product'
        verbose_name_plural = _('record products')
