from dal_select2.widgets import ModelSelect2
from django.forms import ModelChoiceField


class OutcomeCreateFormField(ModelChoiceField):
    widget = ModelSelect2(
        url='outcomes:autocomplete',
        attrs={
            'data-placeholder': 'Outcome..',
        },
    )
