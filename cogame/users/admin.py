from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin
from users.forms import UserCreationForm, UserChangeForm
from users.models import User

__author__ = 'eraldo'


class UserAdmin(AuthUserAdmin):
    add_form = UserCreationForm
    form = UserCreationForm


admin.site.register(User, UserAdmin)
