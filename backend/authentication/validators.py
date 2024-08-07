from django.core.validators import RegexValidator

username_regex = RegexValidator(
    regex=r'^[a-z\d\_]+$',
    message="Enter only lowercase letters, numbers, and underscores. Uppercase letters are not allowed.",
    code='invalid_username'
)
email_regex = RegexValidator(
    regex=r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$',
    message="Enter a valid email address in the format example@example.com.",
    code='invalid_email'
)
phone_regex = RegexValidator(
    regex=r'^\+?1?\d{9,15}$',
    message="Phone number must be entered in the format: '+91'. Up to 13 digits allowed.",
    code='invalid_phone_number'
)