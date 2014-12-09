from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field
from django.forms import ModelForm
from markitup.widgets import MarkItUpWidget
from lib.crispy import CancelButton, SaveButton
from news.models import NewsBlock

__author__ = 'eraldo'


class NewsBlockForm(ModelForm):
    class Meta:
        model = NewsBlock
        fields = ['name', 'content', 'date', 'sticky']
        widgets = {
            'content': MarkItUpWidget(),
        }

    helper = FormHelper()
    helper.layout = Layout(
        Field('name', autofocus='True'),
        Field('date'),
        Field('sticky'),
        Field('content', rows=20),
        SaveButton(),
        CancelButton(),
    )
