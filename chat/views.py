from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import filters
from rest_framework import decorators, filters, request, viewsets
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from .models import Message
from .serializers import ChatSerializer

class ChatViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = ChatSerializer

    search_fields = ["id"]
    ordering_fields = ["id"]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = {
        "user": [
            "exact"
        ],  # filter by the value field of the post_value relationship
    }



def index(request):
    return render(request, "chat/index.html")


def room(request, room_name):
    return render(request, "chat/room.html", {"room_name": room_name})