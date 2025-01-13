from django.shortcuts import render, redirect
from .models import tasks
from .forms import TaskForm, UserForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


@login_required(login_url="signin")
def LandingPage(request):
    data = tasks.objects.all()
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
        print("bahira")
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

    return render(request, "Tasks/login.html", context)


def SignIn(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        if User.objects.get(username=username):
            print("exist")
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


# Create your views here.
