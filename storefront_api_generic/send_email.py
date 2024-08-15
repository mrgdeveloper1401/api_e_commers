from django.core.mail import send_mail
from storefront_api_generic.email_config import EMAIL_HOST_USER


def send_email(user, code):
    subject = 'verify email'
    message = f'equal code for verify email is {code}'
    from_email = EMAIL_HOST_USER
    recipient_list = [user.email]
    send_mail(subject=subject, message=message, from_email=from_email, recipient_list=recipient_list)
