"""
URL configuration for To_Do project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path("Add-Task/", views.AddTask, name="add-task"),
    path("edit-Task/<str:pk>", views.EditTask, name="edit-task"),
    path("Delete-Task/<str:pk>", views.DeleteTask, name="delete-task"),
    path("logout/", views.LogoutUser, name="logout"),
    path("validation/", views.EmailVerification, name="validation"),
]
