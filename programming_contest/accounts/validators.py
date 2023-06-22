from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validate_gmail_email(value):
    if not value.endswith('@gmail.com'):
        raise ValidationError(_('Only gmail.com email addresses are allowed.'), params={'value': value})