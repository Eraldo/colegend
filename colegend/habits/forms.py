from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field
from django.forms import ModelForm
from habits.models import Habit
from lib.crispy import CancelButton, SaveButton

__author__ = 'eraldo'


class HabitForm(ModelForm):
    class Meta:
        model = Habit
        fields = ['routine', 'name', 'description', 'order', 'tags']

    helper = FormHelper()
    helper.layout = Layout(
        Field('routine'),
        Field('name', autofocus='True'),
        Field('description'),
        SaveButton(),
        CancelButton(),
    )
