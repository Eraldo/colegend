from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field
from django.forms import ModelForm
from markitup.widgets import MarkItUpWidget
from lib.crispy import SaveButton, CancelButton
from tags.models import Tag

__author__ = 'eraldo'


class TagForm(ModelForm):
    class Meta:
        model = Tag
        fields = ['name', 'description', 'category']
        widgets = {
            'description': MarkItUpWidget(),
        }

    helper = FormHelper()
    helper.layout = Layout(
        Field('name', autofocus='True'),
        Field('description'),
        Field('category'),
        SaveButton(),
        CancelButton(),
    )
