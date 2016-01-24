from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Field
from django import forms

from .models import Journal


class JournalForm(forms.ModelForm):
    class Meta:
        model = Journal
        fields = [
            # 'name',
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            # Field('name'),
        )
        self.helper.add_input(Submit('save', 'Save'))
