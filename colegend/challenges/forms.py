from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field
from django.forms import ModelForm
from markitup.widgets import MarkItUpWidget
from challenges.models import Challenge
from lib.crispy import SaveButton, CancelButton

__author__ = 'eraldo'


class ChallengeForm(ModelForm):
    class Meta:
        model = Challenge
        fields = ['name', 'content', 'category', 'source']
        widgets = {
            'content': MarkItUpWidget(),
        }

    helper = FormHelper()
    helper.layout = Layout(
        Field('name', autofocus='True', placeholder="Challenge title."),
        Field('content', placeholder="Challenge description..", rows=20),
        Field('category'),
        Field('source', rows=2),
        SaveButton(),
        CancelButton(),
    )
