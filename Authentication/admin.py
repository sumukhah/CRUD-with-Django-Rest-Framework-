from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


class CustomAdmin(admin.ModelAdmin):
    list_display = ['email', 'name']

admin.site.register(User, CustomAdmin)