from django.core.mail import send_mail
from django.conf import settings
from huey import crontab
from huey import Huey
from huey.contrib.djhuey import task
from datetime import timedelta
from django.utils import timezone

huey = Huey("To_Do")


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


@huey.task()
def alert():
    print("hello")


def schedule_task_after_hours(number_of_hours):

    run_at = timezone.now() + timedelta(hours=number_of_hours)
    print("bitra gayo")
    print("eta", run_at)

    alert.schedule(eta=run_at)
