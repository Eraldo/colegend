from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field
from django.forms import ModelForm
from lib.crispy import SaveButton, CancelButton
from notifications.models import Notification

__author__ = 'eraldo'


class NotificationForm(ModelForm):
    class Meta:
        model = Notification
        fields = ['name', 'description', 'read']

    helper = FormHelper()
    helper.layout = Layout(
        Field('name', autofocus='True'),
        Field('description'),
        SaveButton(),
        CancelButton(),
    )
