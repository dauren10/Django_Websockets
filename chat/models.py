from django.db import models
from core import settings
from django.contrib.auth.models import User
class Message(models.Model):
    recipient = models.ForeignKey(User, on_delete=models.CASCADE,related_name="user_recipient")
    user =  models.ForeignKey(User, on_delete=models.CASCADE,related_name="user_sender")
    created_at = models.DateTimeField(auto_now=True)
    message = models.TextField()