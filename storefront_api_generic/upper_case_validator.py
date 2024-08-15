from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError


class UpperCaseValidator:
    def validate(self, password, user=None):
        if not any(char.isupper() for char in password):
            raise ValidationError(
                _('Password must have at least one uppercase character'),
                code='password not upper',
            )

    def get_help_text(self):
        return _('Password must have at least one uppercase character')
