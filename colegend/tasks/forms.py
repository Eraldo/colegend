from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field, Div
from django.forms import ModelForm
from markitup.widgets import MarkItUpWidget
from tasks.models import Task

__author__ = 'eraldo'


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['project', 'name', 'description', 'status', 'priority', 'date', 'deadline', 'tags']
        widgets = {
            'description': MarkItUpWidget(),
        }

    helper = FormHelper()
    helper.layout = Layout(
        Div(
            Field('name', autofocus='True', wrapper_class="col-md-8"),
            Field('project', wrapper_class="col-md-4"),
            css_class="row",
        ),
        Field('description'),
        Div(
            Field('status', wrapper_class="col-md-3"),
            Field('priority', wrapper_class="col-md-3"),
            Field('date', wrapper_class="col-md-3"),
            Field('deadline', wrapper_class="col-md-3"),
            css_class="row",
        ),
        Field('tags'),
    )
    helper.add_input(Submit('save', 'Save'))
