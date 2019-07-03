from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User

class CustomAdmin(admin.ModelAdmin):
    list_display = ['email', 'name', 'id']

admin.site.register(User, CustomAdmin)