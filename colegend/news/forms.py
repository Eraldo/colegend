from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field
from django.forms import ModelForm
from challenges.models import Challenge
from news.models import NewsBlock

__author__ = 'eraldo'


class NewsBlockForm(ModelForm):
    class Meta:
        model = NewsBlock
        fields = ['name', 'description', 'date']

    helper = FormHelper()
    helper.layout = Layout(
        Field('name', autofocus='True'),
        Field('description', rows=20),
        Field('date'),
    )
    helper.add_input(Submit('save', 'Save'))
