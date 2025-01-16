from django.core.mail import send_mail
from django.conf import settings


def WelcomeMessage():
    send_mail(
        "Subject here",
        "Here is the message.",
        settings.EMAIL_HOST_USER,
        ["ronishmakaju12345@gmail.com"],
        fail_silently=False,
    )
