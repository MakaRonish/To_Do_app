from django.db import models
import uuid

# Create your models here.


class tasks(models.Model):
    type = [
        ("w", "Work"),
        ("p", "Personal"),
        ("o", "Others"),
    ]
    id = models.UUIDField(
        default=uuid.uuid4, primary_key=True, unique=True, editable=True
    )
    created = models.DateField(auto_now_add=True)
    task = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True, max_length=500)
    completed = models.BooleanField(default=False)
    deadline = models.DateTimeField(null=True, blank=True)
    category = models.CharField(max_length=1, choices=type)

    def __str__(self):
        return self.task
