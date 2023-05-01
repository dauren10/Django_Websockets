from django.db import models
from core import settings
from django.contrib.auth.models import User
class Chat(models.Model):
    user =  models.ForeignKey(User, on_delete=models.CASCADE,)
    created_at = models.DateTimeField(auto_now=True)
    message = models.TextField()