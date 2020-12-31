from django.db import models
from django.contrib.auth.models import User


class Challenge(models.Model):
    name = models.CharField(max_length=150)
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)