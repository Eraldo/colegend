from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Field
from django import forms

from colegend.community.models import Duo, Clan, Tribe


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


class ClanForm(forms.ModelForm):
    class Meta:
        model = Clan
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


class TribeForm(forms.ModelForm):
    class Meta:
        model = Tribe
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
