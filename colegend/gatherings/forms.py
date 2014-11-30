from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field
from django.forms import ModelForm
from gatherings.models import Gathering

__author__ = 'eraldo'


class GatheringForm(ModelForm):
    class Meta:
        model = Gathering
        fields = ['start', 'end', 'location', 'online']

    helper = FormHelper()
    helper.layout = Layout(
        Field('start'),
        Field('end'),
        Field('location'),
        Field('online'),
    )
    helper.add_input(Submit('save', 'Save'))
