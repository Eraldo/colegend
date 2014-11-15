from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field
from django.forms import ModelForm
from markitup.widgets import MarkItUpWidget
from news.models import NewsBlock

__author__ = 'eraldo'


class NewsBlockForm(ModelForm):
    class Meta:
        model = NewsBlock
        fields = ['name', 'content', 'date']
        widgets = {
            'content': MarkItUpWidget(),
        }

    helper = FormHelper()
    helper.layout = Layout(
        Field('name', autofocus='True'),
        Field('content', rows=20),
        Field('date'),
    )
    helper.add_input(Submit('save', 'Save'))
