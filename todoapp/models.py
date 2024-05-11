from django.contrib.auth.models import User
from django.db import models
import uuid

class Note(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id = models.UUIDField(unique=True, primary_key=True, editable=False, default=uuid.uuid4)
    todo_name = models.CharField(max_length=250)
    body = models.TextField(null=True, blank=True)
    status = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)



    def __str__(self):
        return self.todo_name

