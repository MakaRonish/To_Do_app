from django.forms import ModelForm
from django.contrib.auth.models import User
from django import forms
from .models import tasks


class TaskForm(ModelForm):
    class Meta:
        model = tasks
        fields = ["task", "description", "deadline", "category"]
        widgets = {"deadline": forms.DateInput(attrs={"type": "date"})}


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email", "password"]
