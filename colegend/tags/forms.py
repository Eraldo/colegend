from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Field
from django import forms

from .models import Tag


# class TagForm(OwnedModelForm):
class TagForm(forms.ModelForm):

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

    def clean_owner(self):
        owner = self.cleaned_data.get('owner')
        if not owner == self.owner:
            message = 'You need to be the owner.'
            self.add_error(None, message)
        return owner
