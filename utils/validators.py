from django.core.exceptions import ValidationError
import re

def validate_phone_number(value):
    phone_regex = re.compile(r'^\+?1?\d{9,15}$')
    if not phone_regex.match(value):
        raise ValidationError('Phone number must be entered in the format: "+910123456789". Up to 15 digits allowed.')

def validate_year(value):
    if not value.isdigit() or len(value) != 4:
        raise ValidationError('Year must be a four-digit number.')
