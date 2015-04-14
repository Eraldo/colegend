from autocomplete_light import MultipleChoiceWidget
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Row
from django.forms import ModelForm
from markitup.widgets import MarkItUpWidget
from lib.crispy import CancelButton, SaveButton
from projects.models import Project

__author__ = 'eraldo'


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'description', 'status', 'date', 'deadline', 'tags', 'category']
        widgets = {
            'description': MarkItUpWidget(),
            'tags': MultipleChoiceWidget(autocomplete="TagAutocomplete"),
        }

    helper = FormHelper()
    helper.layout = Layout(
        Field('name', autofocus='True'),
        Field('description'),
        Row(
            Field('status', wrapper_class="col-md-3"),
            Field('date', wrapper_class="col-md-3"),
            Field('deadline', wrapper_class="col-md-3"),
            Field('category', wrapper_class="col-md-3"),
        ),
        Field('tags'),
        SaveButton(),
        CancelButton(),
    )
