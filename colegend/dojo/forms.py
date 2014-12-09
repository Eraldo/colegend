from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field
from django.forms import ModelForm
from markitup.widgets import MarkItUpWidget
from dojo.models import Module
from lib.crispy import SaveButton, CancelButton

__author__ = 'eraldo'


class ModuleForm(ModelForm):
    class Meta:
        model = Module
        fields = ['name', 'description', 'content', 'category', 'source']
        widgets = {
            'content': MarkItUpWidget(),
        }

    helper = FormHelper()
    helper.layout = Layout(
        Field('name', autofocus='True', placeholder="Module title."),
        Field('description', placeholder="Module essence.", rows=4),
        Field('content', placeholder="Module content.", rows=20),
        Field('category'),
        Field('source', rows=2),
        SaveButton(),
        CancelButton(),
    )

