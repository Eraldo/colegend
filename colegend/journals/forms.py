from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Div
from django.forms import ModelForm
from markitup.widgets import MarkItUpWidget
from journals.models import DayEntry
from lib.crispy import CancelButton, SaveButton

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
        Div(
            Field('date', wrapper_class="col-md-6"),
            Field('location', wrapper_class="col-md-6"),
            css_class="row",
        ),
        Field('focus', autofocus='True'),
        Field('content', rows="20"),
        SaveButton(),
        CancelButton(),
    )
