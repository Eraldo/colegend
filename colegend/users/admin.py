# -*- coding: utf-8 -*-
from django import forms
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin
from django.contrib.auth.forms import UserChangeForm as AuthUserChangeForm, UserCreationForm as AuthUserCreationForm
from django.utils.translation import ugettext_lazy as _

from .models import User


class UserChangeForm(AuthUserChangeForm):
    class Meta(AuthUserChangeForm.Meta):
        model = User


# class UserCreationForm(AuthUserCreationForm):
#     class Meta(AuthUserCreationForm.Meta):
#         model = User

class UserCreationForm(AuthUserCreationForm):

    error_message = AuthUserCreationForm.error_messages.update({
        'duplicate_username': 'This username has already been taken.'
    })

    class Meta(AuthUserCreationForm.Meta):
        model = User

    def clean_username(self):
        username = self.cleaned_data["username"]
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError(self.error_messages['duplicate_username'])


class UserInline(admin.TabularInline):
    fields = ['username', 'email']
    model = User
    extra = 0
    show_change_link = True
    # max_num = 4


class UserCheckpointInline(admin.TabularInline):
    model = User.checkpoints.through
    extra = 0
    show_change_link = True


@admin.register(User)
class UserAdmin(AuthUserAdmin):
    fieldsets = (
        (None, {
            'fields': (
                'username', 'password'
            )
        }),
        (_('Personal info'), {
            'fields': (
                'name', 'gender', 'birthday',
                'email', 'phone', 'address',
                'occupation'
            )
        }),
        (_('Data'), {
            'fields': (
                'avatar', 'purpose', 'status',
                'duo', 'clan', 'tribe', 'mentor'
            )
        }),
        (_('Permissions'), {
            'fields': (
                'is_active', 'is_staff', 'is_superuser',
                'is_premium', 'balance',
                'roles', 'groups', 'user_permissions',
            )
        }),
        (_('Important dates'), {
            'fields': ('last_login', 'date_joined')
        }),
        (_('Meta'), {
            'fields': ('notes',),
            'classes': ('collapse',),
        }),
    )
    list_display = ('username', 'name', 'email', 'phone', 'balance', 'is_premium', 'is_staff', 'date_joined')
    list_filter = ('is_premium', 'is_staff', 'is_superuser', 'is_active', 'roles', 'checkpoints', 'groups', 'date_joined', 'last_login')
    filter_horizontal = ('roles', 'groups', 'user_permissions')
    search_fields = ['name']
    form = UserChangeForm
    add_form = UserCreationForm
    inlines = [UserCheckpointInline]
