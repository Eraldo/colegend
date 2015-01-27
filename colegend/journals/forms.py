from autocomplete_light import MultipleChoiceWidget
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Row
from django.forms import ModelForm
from markitup.widgets import MarkItUpWidget
from journals.models import DayEntry, Journal
from lib.crispy import CancelButton, SaveButton

__author__ = 'eraldo'


class JournalForm(ModelForm):
    class Meta:
        model = Journal
        fields = ['template', 'topic_of_the_year']
        widgets = {
            'template': MarkItUpWidget(),
        }

    helper = FormHelper()
    helper.layout = Layout(
        Field('topic_of_the_year', autofocus='True'),
        Field('template'),
        SaveButton(),
        CancelButton(),
    )


class DayEntryForm(ModelForm):
    class Meta:
        model = DayEntry
        fields = ['date', 'location', 'focus', 'tags', 'content']
        widgets = {
            'content': MarkItUpWidget(),
            'tags': MultipleChoiceWidget(autocomplete="TagAutocomplete"),
        }

    helper = FormHelper()
    helper.layout = Layout(
        Row(
            Field('date', wrapper_class="col-md-6"),
            Field('location', wrapper_class="col-md-6"),
        ),
        Field('focus', autofocus='True'),
        Field('content', rows="20"),
        Field('tags'),
        SaveButton(),
        CancelButton(),
    )
