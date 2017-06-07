from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Field
from django import forms

from colegend.users.models import User

__author__ = 'Eraldo Energy'


class WelcomeEmailForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'email',
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Field('email', placeholder="Enter Email", autofocus=True, required=True),
        )
        self.helper.form_tag = False
        self.helper.form_show_labels = False


class WelcomePasswordForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = [
            'email',
            'password',
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Field('email', type="hidden"),
            Field('password', placeholder="Enter Passphrase", autocomplete='off', autofocus=True),
        )
        self.helper.form_tag = False
        self.helper.form_show_labels = False
