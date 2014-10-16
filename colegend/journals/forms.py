from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field
from django.forms import ModelForm
from journals.models import DayEntry
from tags.models import Tag

__author__ = 'eraldo'


class DayEntryForm(ModelForm):
    class Meta:
        model = DayEntry
        fields = ['date', 'location', 'text']

    helper = FormHelper()
    helper.layout = Layout(
        Field('date'),
        Field('location'),
        Field('text', autofocus='True', rows="20")
    )
    helper.add_input(Submit('save', 'Save'))
