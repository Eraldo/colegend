from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Field
from django import forms

from colegend.core.forms import OwnedModelForm
from .models import Vision


class VisionForm(OwnedModelForm):
    class Meta:
        model = Vision
        fields = [
            'owner',
            'image',
            'content',
        ]

    def __init__(self, *args, **kwargs):
        self.owner = kwargs.pop('owner', None)
        super().__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.layout = Layout(
            Field('owner', type="hidden"),
            Field('image'),
            Field('content'),
        )
        self.helper.add_input(Submit('save', 'Save'))
