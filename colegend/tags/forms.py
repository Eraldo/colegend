from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field
from django.forms import ModelForm
from markitup.widgets import MarkItUpWidget
from tags.models import Tag

__author__ = 'eraldo'


class TagForm(ModelForm):
    class Meta:
        model = Tag
        fields = ['name', 'description']
        widgets = {
            'description': MarkItUpWidget(),
        }

    helper = FormHelper()
    helper.layout = Layout(
        Field('name', autofocus='True'),
        Field('description'),
    )
    helper.add_input(Submit('save', 'Save'))
