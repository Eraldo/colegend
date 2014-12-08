from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field, Div
from django.forms import ModelForm
from markitup.widgets import MarkItUpWidget
from projects.models import Project

__author__ = 'eraldo'


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'description', 'status', 'priority', 'deadline', 'tags']
        widgets = {
            'description': MarkItUpWidget(),
        }

    helper = FormHelper()
    helper.layout = Layout(
        Field('name', autofocus='True'),
        Field('description'),
        Div(
            Field('status', wrapper_class="col-md-4"),
            Field('priority', wrapper_class="col-md-4"),
            Field('deadline', wrapper_class="col-md-4"),
            css_class="row",
        ),
    )
    helper.add_input(Submit('save', 'Save'))
