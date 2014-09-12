from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin
from users.forms import UserCreationForm
from users.models import User
from django.utils.translation import ugettext_lazy as _

__author__ = 'eraldo'


class UserAdmin(AuthUserAdmin):
    add_form = UserCreationForm

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'gender', 'birthday',)}),
        (_('Contact info'), {'fields': ('email', 'phone_number', 'street', 'postal_code', 'city', 'country')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )


admin.site.register(User, UserAdmin)
