from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin
from lib.admin import EmailMixin
from users.forms import UserCreationForm
from users.models import User, Contact, Profile, Settings
from django.utils.translation import ugettext_lazy as _

__author__ = 'eraldo'


class ContactInline(admin.StackedInline):
    model = Contact
    verbose_name_plural = "Contact"


class SettingsInline(admin.StackedInline):
    model = Settings


class ProfileInline(admin.StackedInline):
    model = Profile


class UserAdmin(EmailMixin, AuthUserAdmin):
    add_form = UserCreationForm
    list_display = ('username', 'email_link', 'get_full_name', 'is_accepted', 'is_tester', 'is_staff')
    list_filter = ('is_active', 'is_accepted', 'is_tester', 'is_staff', 'is_superuser', 'groups')

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        (_('Notes'), {
            'classes': ('collapse',),
            'fields': ('notes',)}),
        (_('Roles'), {
            'classes': ('collapse',),
            'fields': ('is_active', 'is_accepted', 'is_tester', 'is_staff', 'is_superuser')}),
        (_('Permissions'), {
            'classes': ('collapse',),
            'fields': ('groups', 'user_permissions')}),
        (_('Dates'), {
            'classes': ('collapse',),
            'fields': ('last_login', 'date_accepted', 'date_joined')}),
    )
    inlines = [ContactInline, SettingsInline, ProfileInline]


admin.site.register(User, UserAdmin)


class ContactAdmin(EmailMixin, admin.ModelAdmin):
    list_display = ['get_name', 'email_link', 'owner']
    search_fields = ['owner__first_name', 'owner__last_name']
    list_filter = ['owner']
    readonly_fields = ['first_name', 'last_name']

    fieldsets = (
        (None, {'fields': ('owner',)}),
        (None, {
            'description': '<div class="help">Use the User admin to change the name and email address.</div>',
            'fields': ('first_name', 'last_name', 'email_link', 'phone_number'), }),
        (_('Address'), {'fields': ('street', 'postal_code', 'city', 'country')}),
        (_('Details'), {'fields': ('gender', 'birthday')}),
    )


admin.site.register(Contact, ContactAdmin)


class ProfileAdmin(admin.ModelAdmin):
    list_filter = ['owner']

    fieldsets = (
        (None, {'fields': ('owner',)}),
        (_('Questions'),
         {'fields': ('origin', 'referrer', 'experience', 'motivation', 'change', 'drive', 'expectations', 'other')}),
        (_('Guidelines'), {'fields': ('stop', 'discretion', 'responsibility', 'appreciation', 'terms')})
    )


admin.site.register(Profile, ProfileAdmin)


class SettingsAdmin(admin.ModelAdmin):
    list_filter = ['owner']

    fieldsets = (
        (None, {'fields': ('owner',)}),
        (_('General Settings'),
         {'fields': ('language', 'day_start', 'sound')}),
        (_('Journal Settings'),
         {'fields': ('journal_entry_template',)}),
    )


admin.site.register(Settings, SettingsAdmin)
