from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field
from django.forms import ModelForm
from routines.models import Routine

__author__ = 'eraldo'


class RoutineForm(ModelForm):
    class Meta:
        model = Routine
        fields = ['name', 'description', 'type', 'tags']

    helper = FormHelper()
    helper.layout = Layout(
        Field('name', autofocus='True'),
        Field('description'),
    )
    helper.add_input(Submit('save', 'Save'))
