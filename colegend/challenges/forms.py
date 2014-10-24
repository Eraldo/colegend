from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field
from django.forms import ModelForm
from challenges.models import Challenge

__author__ = 'eraldo'


class ChallengeForm(ModelForm):
    class Meta:
        model = Challenge
        fields = ['name', 'description', 'category', 'source']

    helper = FormHelper()
    helper.layout = Layout(
        Field('name', autofocus='True', placeholder="Challenge title."),
        Field('description', placeholder="Challenge description.", rows=20),
        Field('category'),
        Field('source', rows=2),
    )
    helper.add_input(Submit('save', 'Save'))
