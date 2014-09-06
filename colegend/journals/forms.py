from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field
from django.forms import ModelForm
from journals.models import DayEntry
from tags.models import Tag

__author__ = 'eraldo'


class DayEntryForm(ModelForm):
    class Meta:
        model = DayEntry
        fields = ['date', 'text']

    helper = FormHelper()
    helper.layout = Layout(
        Field('date'),
        Field('text', autofocus='True')
    )
    helper.add_input(Submit('save', 'Save'))
