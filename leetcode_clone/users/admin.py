from django.contrib import admin
from .models import CustomUser

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name')  # Add required fields here

admin.site.register(CustomUser, CustomUserAdmin)
