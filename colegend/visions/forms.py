from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field
from django import forms
from django.forms import ModelForm
from markitup.widgets import MarkItUpWidget
from visions.models import Vision

__author__ = 'eraldo'


class VisionForm(ModelForm):
    you = forms.BooleanField(
        help_text="The vision is about you. What you do and what you want.",
        initial=False
    )
    present = forms.BooleanField(
        help_text="Your vision is formulated in the present tense: 'I live in ...'",
        initial=False
    )

    class Meta:
        model = Vision
        fields = ['name', 'content']
        widgets = {
            'content': MarkItUpWidget(),
        }

    helper = FormHelper()
    helper.layout = Layout(
        Field('name', autofocus='True'),
        Field('content', rows="20"),
        Field('you'),
        Field('present'),
    )
    helper.add_input(Submit('save', 'Save'))
