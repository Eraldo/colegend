from dal_select2.widgets import ModelSelect2Multiple
from django.forms import ModelMultipleChoiceField


class TagsCreateFormField(ModelMultipleChoiceField):
    widget = ModelSelect2Multiple(
        url='tags:autocomplete',
        attrs={
            'data-placeholder': 'Tags..',
        },
    )
