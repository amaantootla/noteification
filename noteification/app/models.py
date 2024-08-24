from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    pass


class Tag(models.Model):
    # TODO ensure no Tag of a duplicate name may be created.
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=64)


class Note(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=64)
    content = models.TextField()
    tags = models.ManyToManyField(Tag, related_name="notes")
