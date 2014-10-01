from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field
from django.forms import ModelForm
from dojo.models import Module

__author__ = 'eraldo'


class ModuleForm(ModelForm):
    class Meta:
        model = Module
        fields = ['name', 'description', 'category', 'source']

    helper = FormHelper()
    helper.layout = Layout(
        Field('name', autofocus='True', placeholder="Module title."),
        Field('description', placeholder="Module content."),
        Field('category'),
        Field('source', rows=2),
    )
    helper.add_input(Submit('save', 'Save'))
