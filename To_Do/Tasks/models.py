from django.db import models
import uuid
from django.contrib.auth.models import User

# Create your models here.


class tasks(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    email_varified = models.BooleanField(default=False)
    type = [
        ("Work", "Work"),
        ("Personal", "Personal"),
        ("Others", "Others"),
    ]
    id = models.UUIDField(
        default=uuid.uuid4, primary_key=True, unique=True, editable=True
    )
    created = models.DateField(auto_now_add=True)
    task = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True, max_length=500)
    completed = models.BooleanField(default=False)
    deadline = models.DateTimeField(null=True, blank=True)
    category = models.CharField(max_length=8, choices=type)

    def __str__(self):
        return self.task

    class Meta:
        ordering = ["deadline"]
