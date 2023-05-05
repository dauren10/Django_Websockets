from rest_framework import serializers
from .models import Message

class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['id', 'created_at', 'user', 'message']