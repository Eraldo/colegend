from django import forms
from django.contrib.auth.forms import UserCreationForm as AuthUserCreationForm, UserChangeForm as AuthUserChangeForm
from users.models import User

__author__ = 'eraldo'


class UserForm(forms.ModelForm):
    class Meta:
        # Set this form to use the User model.
        model = User

        # Constrain the UserForm to just these fields.
        fields = ("first_name", "last_name")


class UserCreationForm(AuthUserCreationForm):
    """
    Custom user creation form.
    """

    class Meta(AuthUserCreationForm.Meta):
        model = User

    def clean_username(self):
        """
        Custom username clean method overwrite.

        This is used because django's default implementation hardcodes the auth.user.

        :return: :raise forms.ValidationError:
        """
        username = self.cleaned_data['username']
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError(self.error_messages['duplicate_username'])


class UserChangeForm(AuthUserChangeForm):
    class Meta(AuthUserChangeForm.Meta):
        model = User
