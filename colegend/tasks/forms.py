from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.forms import ModelForm
from tasks.models import Task

__author__ = 'eraldo'


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['project', 'name', 'description', 'status', 'date', 'deadline', 'tags']

    helper = FormHelper()
    helper.add_input(Submit('save', 'Save'))
