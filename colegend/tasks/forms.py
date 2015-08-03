from autocomplete_light import MultipleChoiceWidget, ChoiceWidget
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Row
from django.core.exceptions import ValidationError
from django.forms import ModelForm, HiddenInput
from markitup.widgets import MarkItUpWidget
from lib.crispy import CancelButton, SaveButton
from tasks.models import Task

__author__ = 'eraldo'


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['owner', 'project', 'name', 'description', 'status', 'date', 'deadline', 'tags', 'category']
        widgets = {
            'description': MarkItUpWidget(),
            'tags': MultipleChoiceWidget(autocomplete="TagAutocomplete"),
            'project': ChoiceWidget(autocomplete="ProjectAutocomplete"),
            'owner': HiddenInput
        }

    def clean(self):
        cleaned_data = super().clean()
        status = cleaned_data.get("status")
        # Limit number of maximum "next" tasks.
        if status and status.name == "next":
            max = 16
            # number of other tasks with status next
            current = cleaned_data['owner'].tasks.next().filter(project__isnull=True).exclude(pk=self.instance.pk).count()
            if current >= max:
                raise ValidationError(
                    "You have reached the limit of 'next' tasks! {}/{} Tip: Check if you can set others to 'todo'.".format(
                        current, "8"))

    helper = FormHelper()
    helper.layout = Layout(
        Row(
            Field('name', autofocus='True', wrapper_class="col-md-8"),
            Field('project', wrapper_class="col-md-4"),
        ),
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
