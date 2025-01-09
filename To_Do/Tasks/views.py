from django.shortcuts import render, redirect
from .models import tasks
from .forms import TaskForm


def LandingPage(request):
    data = tasks.objects.all()
    context = {"data": data}
    return render(request, "Tasks/home.html", context)


def AddTask(request):
    form = TaskForm()
    context = {"form": form}
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("landing-page")
    return render(request, "Tasks/addtask.html", context)


# Create your views here.
