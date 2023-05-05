from django.contrib import admin
from .models import Message
# Register your models here.
class ChatAdmin(admin.ModelAdmin):
    list_display = ("id", "recipient", "user","message","created_at")
    ordering = ["id"]
admin.site.register(Message,ChatAdmin)