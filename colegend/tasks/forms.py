from autocomplete_light import MultipleChoiceWidget, ChoiceWidget
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Row
from django.forms import ModelForm
from markitup.widgets import MarkItUpWidget
from lib.crispy import CancelButton, SaveButton
from tasks.models import Task

__author__ = 'eraldo'


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['project', 'name', 'description', 'status', 'date', 'deadline', 'tags']
        widgets = {
            'description': MarkItUpWidget(),
            'tags': MultipleChoiceWidget(autocomplete="TagAutocomplete"),
            'project': ChoiceWidget(autocomplete="ProjectAutocomplete"),

        }

    helper = FormHelper()
    helper.layout = Layout(
        Row(
            Field('name', autofocus='True', wrapper_class="col-md-8"),
            Field('project', wrapper_class="col-md-4"),
        ),
        Field('description'),
        Row(
            Field('status', wrapper_class="col-md-4"),
            Field('date', wrapper_class="col-md-4"),
            Field('deadline', wrapper_class="col-md-4"),
        ),
        Field('tags'),
        SaveButton(),
        CancelButton(),
    )
