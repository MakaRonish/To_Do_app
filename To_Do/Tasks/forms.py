from django.forms import ModelForm
from django import forms
from .models import tasks


class TaskForm:
    class Meta:
        model = tasks
        fields = ["task", "description", "deadline", "category"]
        widgets = {"deadline": forms.DateInput(attrs={"type": "date"})}
