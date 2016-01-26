from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Field

from colegend.core.forms import OwnedModelForm
from .models import Tag


class TagForm(OwnedModelForm):
    class Meta:
        model = Tag
        fields = [
            'owner',
            'name',
            'description',
            'category',
        ]

    def __init__(self, *args, **kwargs):
        self.owner = kwargs.pop('owner', None)
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Field('owner', type='hidden'),
            Field('name'),
            Field('description'),
            Field('category'),
        )
        self.helper.add_input(Submit('save', 'Save'))
