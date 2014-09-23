from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field
from django.forms import ModelForm
from quotes.models import Quote
from tags.models import Tag

__author__ = 'eraldo'


class QuoteForm(ModelForm):
    class Meta:
        model = Quote
        fields = ['name', 'text', 'author', 'category']

    helper = FormHelper()
    helper.layout = Layout(
        Field('name', autofocus='True', placeholder="Some Words"),
        Field('text', placeholder="Some words are more than nothing."),
        Field('author', placeholder='Someone'),
        Field('category'),
    )
    helper.add_input(Submit('save', 'Save'))
