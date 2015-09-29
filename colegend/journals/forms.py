from autocomplete_light import MultipleChoiceWidget
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Row
from django import forms
from django.core.exceptions import ValidationError
from django.forms import ModelForm, HiddenInput
from django.utils import timezone
from markitup.widgets import MarkItUpWidget
from journals.models import DayEntry, Journal, WeekEntry
from lib.crispy import CancelButton, SaveButton, IconButton

__author__ = 'eraldo'


class JournalForm(ModelForm):
    class Meta:
        model = Journal
        fields = ['day_template', 'week_template', 'topic_of_the_year']
        widgets = {
            'day_template': MarkItUpWidget(),
        }

    helper = FormHelper()
    helper.layout = Layout(
        Field('topic_of_the_year', autofocus='True'),
        Field('day_template'),
        Field('week_template'),
        SaveButton(),
        CancelButton(),
    )


class DayEntryForm(ModelForm):
    class Meta:
        model = DayEntry
        fields = ['date', 'location', 'focus', 'tags', 'content']
        widgets = {
            'content': MarkItUpWidget(),
            'tags': MultipleChoiceWidget(autocomplete="TagAutocomplete"),
        }

    helper = FormHelper()
    helper.layout = Layout(
        Row(
            Field('date', wrapper_class="col-md-6"),
            Field('location', wrapper_class="col-md-6"),
        ),
        Field('focus', autofocus='True'),
        Field('content', rows="20"),
        Field('tags'),
        SaveButton(),
        CancelButton(),
    )


class WeekEntryForm(ModelForm):
    class Meta:
        model = WeekEntry
        fields = ['journal', 'date', 'focus', 'tags', 'content']
        widgets = {
            'content': MarkItUpWidget(),
            'tags': MultipleChoiceWidget(autocomplete="TagAutocomplete"),
            'journal': HiddenInput
        }

    def clean(self):
        cleaned_data = super().clean()
        # Check if there is not yet another entry for this week.
        date = cleaned_data["date"]
        # raise Exception(date)
        # # first/last day of that week
        first_day = date - timezone.timedelta(days=date.weekday())
        last_day = first_day + timezone.timedelta(days=6)
        other = cleaned_data["journal"].week_entries.filter(
            date__range=(first_day, last_day)).exclude(pk=self.instance.pk)
        if other.exists():
            raise ValidationError("There is already an entry for this week: {}".format(other))

    helper = FormHelper()
    helper.layout = Layout(
        Row(
            Field('date', wrapper_class="col-md-6"),
        ),
        Field('focus', autofocus='True'),
        Field('content', rows="20"),
        Field('tags'),
        SaveButton(),
        CancelButton(),
    )


class ImportForm(forms.Form):
    text = forms.CharField(
        label="Journal entry/entries to import",
        widget=forms.Textarea,
        help_text="Date format: YYYY-MM-DD or DD.MM.YYYY, Tags are comma separated.",
    )

    def import_entries(self):
        text = self.cleaned_data["text"]

        # Split journal entries
        # import re
        # re.findall('^.*?the', text, re.DOTALL)
        #
        print(text.split("Date:"))


    helper = FormHelper()
    helper.layout = Layout(
        Field('text', rows="20"),
        IconButton("import", "Import", "import", input_type="submit", css_class="btn-primary"),
        CancelButton(),
    )
