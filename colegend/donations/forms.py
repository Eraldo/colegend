from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Field
from django import forms

from .models import Donation


class DonationForm(forms.ModelForm):
    class Meta:
        model = Donation
        fields = [
            'owner',
            'date',
            'amount',
            'notes',
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Field('owner'),
            Field('date'),
            Field('amount'),
            Field('notes', rows=2),
        )
        self.helper.add_input(Submit('save', 'Save'))
