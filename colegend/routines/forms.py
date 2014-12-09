from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Row
from django.forms import ModelForm
from lib.crispy import SaveButton, CancelButton
from routines.models import Routine

__author__ = 'eraldo'


class RoutineForm(ModelForm):
    class Meta:
        model = Routine
        fields = ['name', 'description', 'type', 'tags']

    helper = FormHelper()
    helper.layout = Layout(
        Row(
            Field('name', autofocus='True', wrapper_class="col-md-9"),
            Field('type', wrapper_class="col-md-3"),
        ),
        Field('description'),
        Field('tags'),
        SaveButton(),
        CancelButton(),
    )
