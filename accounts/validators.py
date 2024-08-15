from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_mobile_phone(value):
    from accounts.models import Users
    if Users.objects.filter(mobile_phone=value).exists():
        raise ValidationError(_('this mobile phone already exists'))
