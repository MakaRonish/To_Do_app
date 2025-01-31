from django.shortcuts import render, redirect
from .models import tasks
from .forms import TaskForm, UserForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .signals import WelcomeMessage, EmailVerify, schedule_task_after_hours, huey
import random
from django.utils import timezone
from datetime import timedelta

# assuming huey instance is in huey_instance.py


@login_required(login_url="signin")
def LandingPage(request):
    data = tasks.objects.filter(user=request.user)
    context = {"data": data}
    if request.method == "POST":
        id = request.POST["id"]
        element = tasks.objects.get(id=id)
        if element.completed:
            element.completed = False
            element.save()
        else:
            element.completed = True
            element.save()

        return redirect("landing-page")

    return render(request, "Tasks/home.html", context)


@login_required(login_url="signin")
def AddTask(request):
    form = TaskForm()
    context = {"form": form}
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            deadline = task.deadline
            current_time = timezone.localtime()

            # Calculate 24 hours before the deadline
            time_before_deadline = deadline - timezone.timedelta(hours=24)

            # Calculate the number of hours between the current time and 24 hours before the deadline
            number_of_hour = (
                time_before_deadline - current_time
            ).total_seconds() / 3600

            print("current time", current_time)
            print("deadline time", deadline)
            print("time before deadline", time_before_deadline)
            print("difference", number_of_hour)
            if number_of_hour < 0:
                number_of_hour = 0
            print("number_of_hour", number_of_hour)

            schedule_task_after_hours(number_of_hour)

            task.save()
            return redirect("landing-page")
    return render(request, "Tasks/addtask.html", context)


@login_required(login_url="signin")
def EditTask(request, pk):
    instance = tasks.objects.get(id=pk)
    form = TaskForm(instance=instance)
    context = {"form": form}
    if request.method == "POST":
        form = TaskForm(request.POST, instance=instance)

        if form.is_valid():
            print("valid")
            form.save()
            return redirect("landing-page")
    return render(request, "Tasks/edittask.html", context)


@login_required(login_url="signin")
def DeleteTask(request, pk):
    task = tasks.objects.get(id=pk)
    task.delete()
    return redirect("landing-page")


def Login(request):

    form = UserForm()
    context = {"form": form}
    if request.method == "POST":

        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            login(request, user)
            return redirect("validation")

    return render(request, "Tasks/login.html", context)


def SignIn(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("landing-page")
        else:
            messages.warning(request, "Error wrong credential")

    return render(request, "Tasks/signin.html")


def LogoutUser(request):
    logout(request)

    return redirect("landing-page")


@login_required(login_url="signin")
def EmailVerification(request):
    user = request.user
    email = user.email
    print(email)
    if "random_code" not in request.session:
        random_code = random.randint(1000, 9999)
        request.session["random_code"] = random_code
        EmailVerify(random_code, email)

    if request.method == "POST":
        code = request.POST["code"]

        if code == str(request.session["random_code"]):
            user.email_varified = True
            del request.session["random_code"]
            WelcomeMessage(email)
            return redirect("landing-page")
        else:

            messages.warning(request, "wrong code")

    return render(request, "Tasks/emailvalidation.html")


# Create your views here.
