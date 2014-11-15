from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field
from django.forms import ModelForm
from markitup.widgets import MarkItUpWidget
from journals.models import DayEntry

__author__ = 'eraldo'


class DayEntryForm(ModelForm):
    class Meta:
        model = DayEntry
        fields = ['date', 'location', 'focus', 'content']
        widgets = {
            'content': MarkItUpWidget(),
        }

    helper = FormHelper()
    helper.layout = Layout(
        Field('date'),
        Field('location'),
        Field('focus'),
        Field('content', autofocus='True', rows="20"),
    )
    helper.add_input(Submit('save', 'Save'))
