from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin
from users.forms import UserCreationForm
from users.models import User, Contact, Profile
from django.utils.translation import ugettext_lazy as _

__author__ = 'eraldo'


class UserAdmin(AuthUserAdmin):
    add_form = UserCreationForm

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        # (_('Personal info'), {'fields': ('first_name', 'last_name')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'is_tester',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )


admin.site.register(User, UserAdmin)


class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'user']
    search_fields = ['first_name', 'last_name']
    list_filter = ['user']

    fieldsets = (
        (_('Name'), {'fields': ('first_name', 'last_name')}),
        (_('Details'), {'fields': ('gender', 'birthday')}),
        (_('Contact options'), {'fields': ('email', 'phone_number')}),
        (_('Address'), {'fields': ('street', 'postal_code', 'city', 'country')}),
    )



admin.site.register(Contact, ContactAdmin)


class ProfileAdmin(admin.ModelAdmin):
    # list_display = ['__str__', 'user']
    list_filter = ['user']


admin.site.register(Profile, ProfileAdmin)
