from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin
from users.models import User

__author__ = 'eraldo'


class UserAdmin(AuthUserAdmin):
    pass
admin.site.register(User, UserAdmin)
