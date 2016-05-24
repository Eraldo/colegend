from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Field

from colegend.core.forms import OwnedModelForm
from .models import Outcome


class OutcomeForm(OwnedModelForm):
    class Meta:
        model = Outcome
        fields = [
            'owner',
            'name',
            'description',
            'status',
            'review',
            'inbox',
            'date',
            'deadline',
            'estimate',
        ]

    def __init__(self, *args, **kwargs):
        self.owner = kwargs.pop('owner', None)
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Field('owner', type="hidden"),
            Field('name'),
            Field('description'),
            Field('status'),
            Field('review'),
            Field('inbox'),
            Field('date'),
            Field('deadline'),
            Field('estimate'),
        )
        self.helper.add_input(Submit('save', 'Save'))
