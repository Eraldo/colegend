from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin
from lib.admin import EmailMixin
from users.forms import UserCreationForm
from users.models import User, Contact, Profile
from django.utils.translation import ugettext_lazy as _

__author__ = 'eraldo'


class ContactInline(admin.StackedInline):
    model = Contact
    verbose_name_plural = "Contact"


class UserAdmin(EmailMixin, AuthUserAdmin):
    add_form = UserCreationForm
    readonly_fields = ['first_name', 'last_name']
    list_display = ('username', 'email_link', 'get_full_name', 'is_staff')

    fieldsets = (
        (None, {'fields': ('username', 'password', 'email')}),
        (_('Roles'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'is_tester')}),
        (_('Permissions'), {
            'classes': ('collapse',),
            'fields': ('groups', 'user_permissions')}),
        (_('Dates'), {
            'classes': ('collapse',),
            'fields': ('last_login', 'date_joined')}),
    )
    inlines = [ContactInline]


# admin.site.register(User, AuthUserAdmin)
admin.site.register(User, UserAdmin)


class ContactAdmin(EmailMixin, admin.ModelAdmin):
    list_display = ['name', 'email_link', 'user']
    search_fields = ['first_name', 'last_name']
    list_filter = ['user']

    fieldsets = (
        (None, {'fields': ('user',)}),
        (_('Name'), {'fields': ('first_name', 'last_name')}),
        (_('Details'), {'fields': ('gender', 'birthday')}),
        (_('Contact options'), {
            'fields': ('email_link', 'phone_number'),
            'description': '<div class="help">Use the User admin to change the email address.</div>'}),
        (_('Address'), {'fields': ('street', 'postal_code', 'city', 'country')}),
    )


admin.site.register(Contact, ContactAdmin)


class ProfileAdmin(admin.ModelAdmin):
    # list_display = ['__str__', 'user']
    list_filter = ['user']


admin.site.register(Profile, ProfileAdmin)
