from autocomplete_light import MultipleChoiceWidget
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Row
from django.core.exceptions import ValidationError
from django.forms import ModelForm, HiddenInput
from markitup.widgets import MarkItUpWidget
from lib.crispy import CancelButton, SaveButton
from projects.models import Project

__author__ = 'eraldo'


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['owner', 'name', 'description', 'status', 'date', 'deadline', 'tags', 'category']
        widgets = {
            'description': MarkItUpWidget,
            'tags': MultipleChoiceWidget(autocomplete="TagAutocomplete"),
            'owner': HiddenInput
        }

    def clean(self):
        cleaned_data = super().clean()
        # Limit number of maximum "next" projects.
        if cleaned_data["status"].name == "next":
            max = 8
            # number of other projects with status next
            current = cleaned_data["owner"].projects.next().exclude(pk=self.instance.pk).count()
            if current >= max:
                raise ValidationError(
                    "You have reached the limit of 'next' projects! {}/{} Tip: Check if you can set others to 'todo'.".format(
                        current, "4"))

    helper = FormHelper()
    helper.layout = Layout(
        Field('name', autofocus='True'),
        Field('description'),
        Row(
            Field('status', wrapper_class="col-md-3"),
            Field('date', wrapper_class="col-md-3"),
            Field('deadline', wrapper_class="col-md-3"),
            Field('category', wrapper_class="col-md-3"),
        ),
        Field('tags'),
        SaveButton(),
        CancelButton(),
    )
