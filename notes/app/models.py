from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    pass


class Folder(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="folders")
    name = models.CharField(max_length=16)


class Note(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="notes")
    folder = models.ForeignKey(Folder, on_delete=models.CASCADE, related_name="notes")
    body = models.TextField() # a title is implemented via API routes
    last_updated = models.DateTimeField(auto_now=True)