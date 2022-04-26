from django.contrib import admin
from django.db import models

from .models import MyUser


class MyUserAdmin(admin.ModelAdmin):
    list_display = ['email']
    ordering = ('email',)

    fieldsets = (
        (None, {
            'fields': ('password', 'email', 'is_active', 'is_staff', 'is_superuser', 'last_login')
        }),
    )
    add_fieldsets = (
        (None, {
            'fields': ('password', 'email', 'is_active', 'is_staff', 'is_superuser', 'last_login')
        }),
    )




admin.site.register(MyUser, MyUserAdmin)