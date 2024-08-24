from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django_jalali.db.models import jDateField, jDateTimeField

from accounts.managers import PublishModel
from accounts.managers import UserManager
from core.models import UpdateMixin, SoftDeleteMixin, CreateMixin


# Create your models here.
class Users(AbstractUser, UpdateMixin, SoftDeleteMixin):
    email = models.EmailField(_("email address"), blank=True)
    mobile_phone = models.CharField(_("mobile phone"), max_length=15, blank=True, unique=True)
    verify_account = models.BooleanField(_('verify account'), default=False)
    sheba_number = models.CharField(_('sheba number'), max_length=24, blank=True, null=True,
                                    help_text='24 length number, start width IR')
    is_accepted_sheba_number = models.BooleanField(default=False)
    bio = models.CharField(_('bio'), max_length=255, blank=True, null=True)
    date_joined = jDateTimeField(_('date joined'), auto_now_add=True, blank=True, null=True)
    birth_date = jDateField(_("birth day"), blank=True, null=True)
    username = None

    class Gender(models.TextChoices):
        MALE = 'male', _('male')
        FEMALE = 'Female', _('female')

    gender = models.CharField(_("gender"), choices=Gender.choices, max_length=6, blank=True, null=True)
    image = models.ForeignKey('images.Image', blank=True, null=True, on_delete=models.PROTECT,
                              related_name='image_user')

    objects = UserManager()

    USERNAME_FIELD = 'mobile_phone'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    class Meta:
        db_table = 'user'
        verbose_name_plural = _('users')
        verbose_name = _('user')


class PublicNotifications(UpdateMixin, CreateMixin, SoftDeleteMixin):
    title = models.CharField(_('title'), max_length=255)
    description = models.TextField(_('description'))
    image = models.ForeignKey('images.Image', on_delete=models.PROTECT, related_name='public_notification',
                              blank=True, null=True)
    url = models.URLField(_('url'), blank=True, null=True)
    is_active = models.BooleanField(_('is active'), default=True)
    is_read = models.BooleanField(default=False)

    objects = PublishModel()

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'public_notifications'
        verbose_name = _('public notification')
        verbose_name_plural = _('public notifications')


class MobileVerify(CreateMixin):
    mobile_phone = models.CharField(_("mobile phone"), max_length=15)
    code = models.CharField(_("code"), max_length=9)
    expired_code = jDateTimeField(_('expired code'), blank=True, null=True)

    def __str__(self):
        return f'{self.mobile_phone} -- {self.code} {self.expired_code}'

    class Meta:
        db_table = 'mobile_verify'
        verbose_name = _('mobile verify')
        verbose_name_plural = _('mobile verify')
