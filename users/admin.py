# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin
from django.contrib.auth.forms import UserChangeForm as AuthUserChangeForm, UserCreationForm as AuthUserCreationForm
from .models import User


class UserChangeForm(AuthUserChangeForm):
    class Meta(AuthUserChangeForm.Meta):
        model = User


class UserCreationForm(AuthUserCreationForm):
    class Meta(AuthUserCreationForm.Meta):
        model = User


@admin.register(User)
class UserAdmin(AuthUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
