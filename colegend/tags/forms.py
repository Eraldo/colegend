from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.forms import ModelForm
from tags.models import Tag
from tasks.models import Task

__author__ = 'eraldo'


class TagForm(ModelForm):
    class Meta:
        model = Tag
        fields = ['name', 'description']

    helper = FormHelper()
    helper.form_method = 'POST'
    helper.add_input(Submit('save', 'Save'))
