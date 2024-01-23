# users/admin.py

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, WorkerProfile, OwnerPublish

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['username', 'email', 'is_owner', 'is_worker']

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(OwnerPublish)
admin.site.register(WorkerProfile)