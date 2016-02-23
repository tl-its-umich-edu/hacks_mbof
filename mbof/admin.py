from django.contrib import admin

from .models import Message, Role, User

admin.site.register(Message)
admin.site.register(Role)
admin.site.register(User)
