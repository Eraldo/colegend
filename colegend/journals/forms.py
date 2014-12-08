from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field, Div
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
        Div(
            Field('date', wrapper_class="col-md-6"),
            Field('location', wrapper_class="col-md-6"),
            css_class="row",
        ),
        Field('focus', autofocus='True'),
        Field('content', rows="20"),
    )
    helper.add_input(Submit('save', 'Save'))
