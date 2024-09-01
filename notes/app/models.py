from django.db import models
from django.contrib.auth.models import AbstractUser

import io

# Create your models here.

class User(AbstractUser):
    pass


class Note(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="notes")
    body = models.TextField() # a title is implemented via API routes
    last_updated = models.DateTimeField(auto_now=True)

    def preview(self):
         # UI purposes
         return io.StringIO(self.body).readline().strip()[:16] # https://stackoverflow.com/a/7472878