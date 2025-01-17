from django.core.mail import send_mail
from django.conf import settings


def EmailVerify(code, receiver):
    message = f"Thank you for signnig up your code is {code}"
    send_mail(
        "Email Verification",
        message,
        settings.EMAIL_HOST_USER,
        [receiver],
        fail_silently=False,
    )


def WelcomeMessage(receiver):
    send_mail(
        "Subject here",
        "Here is the message.",
        settings.EMAIL_HOST_USER,
        [receiver],
        fail_silently=False,
    )
