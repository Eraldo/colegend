from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field
from django.forms import ModelForm
from visions.models import Vision

__author__ = 'eraldo'


class VisionForm(ModelForm):
    class Meta:
        model = Vision
        fields = ['name', 'description']

    helper = FormHelper()
    helper.layout = Layout(
        Field('name', autofocus='True')
    )
    helper.add_input(Submit('save', 'Save'))
