# -*- coding: utf-8 -*-
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin
from django.contrib.auth.forms import UserChangeForm as AuthUserChangeForm, UserCreationForm as AuthUserCreationForm
from django.utils.translation import ugettext_lazy as _

from .models import User


class UserChangeForm(AuthUserChangeForm):
    class Meta(AuthUserChangeForm.Meta):
        model = User


class UserCreationForm(AuthUserCreationForm):
    class Meta(AuthUserCreationForm.Meta):
        model = User


@admin.register(User)
class UserAdmin(AuthUserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('name', 'gender', 'birthday', 'email', 'phone', 'address', 'occupation')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'checkpoints')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    list_display = ('username', 'name', 'email', 'phone', 'is_staff')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'checkpoints')
    filter_horizontal = ('checkpoints',)
    form = UserChangeForm
    add_form = UserCreationForm
