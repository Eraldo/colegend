from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field
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
        Field('project'),
        Field('name', autofocus='True'),
        Field('description'),
        Field('status'),
        Field('priority'),
        Field('date'),
        Field('deadline'),
        Field('tags'),
    )
    helper.add_input(Submit('save', 'Save'))
