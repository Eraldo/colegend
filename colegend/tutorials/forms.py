from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field
from django.forms import ModelForm
from markitup.widgets import MarkItUpWidget
from lib.crispy import CancelButton, SaveButton
from tutorials.models import Tutorial

__author__ = 'eraldo'


class TutorialForm(ModelForm):
    class Meta:
        model = Tutorial
        fields = ['name', 'description']
        widgets = {
            'description': MarkItUpWidget(),
        }

    helper = FormHelper()
    helper.layout = Layout(
        Field('name', autofocus='True', placeholder="Tutorial title."),
        Field('description', placeholder="Tutorial description.", rows=20),
        SaveButton(),
        CancelButton(),
    )
