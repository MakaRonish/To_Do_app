from django.shortcuts import render

def LandingPage(request):
    return render(request,'Tasks/home.html')

def AddTask(request):
    return render(request,'Tasks/addtask.html')

# Create your views here.
