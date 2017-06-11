from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Field
from django import forms

from colegend.community.models import Duo


class DuoForm(forms.ModelForm):
    class Meta:
        model = Duo
        fields = [
            'name',
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.layout = Layout(
            Field('name'),
        )
        self.helper.add_input(Submit('save', 'Save'))
