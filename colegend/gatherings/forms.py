from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field, Div
from django.core.exceptions import ValidationError
from django.forms import ModelForm
from gatherings.models import Gathering

__author__ = 'eraldo'


class GatheringForm(ModelForm):
    class Meta:
        model = Gathering
        fields = ['start', 'end', 'location', 'online']

    helper = FormHelper()
    helper.layout = Layout(
        Div(
            Field('start', wrapper_class="col-md-6"),
            Field('end', wrapper_class="col-md-6"),
            css_class="row",
        ),
        Field('location'),
        Field('online'),
    )
    helper.add_input(Submit('save', 'Save'))

    def clean_end(self):
        """
        Making sure the end date is after the start date.
        """
        end = self.cleaned_data['end']
        if end <= self.cleaned_data['start']:
            raise ValidationError("The end time needs to be after the start time.")
        return end
