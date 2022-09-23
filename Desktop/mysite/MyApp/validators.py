from django.core.validators import RegexValidator


def phone_number_validator():
    phone_message = 'Phone number must be entered in the format: 03xxxxxxxxx'
    phone_regex = RegexValidator(regex=r'^(03)\d{9}$', message=phone_message)
    return phone_regex