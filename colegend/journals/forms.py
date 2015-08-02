from autocomplete_light import MultipleChoiceWidget
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Row
from django.forms import ModelForm
from markitup.widgets import MarkItUpWidget
from journals.models import DayEntry, Journal
from lib.crispy import CancelButton, SaveButton

__author__ = 'eraldo'


class JournalForm(ModelForm):
    class Meta:
        model = Journal
        fields = ['template', 'topic_of_the_year']
        widgets = {
            'template': MarkItUpWidget(),
        }

    helper = FormHelper()
    helper.layout = Layout(
        Field('topic_of_the_year', autofocus='True'),
        Field('template'),
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


# class WeekEntryForm(ModelForm):
#     class Meta:
#         model = WeekEntry
#         fields = ['journal', 'date', 'focus', 'tags', 'content']
#         widgets = {
#             'content': MarkItUpWidget(),
#             'tags': MultipleChoiceWidget(autocomplete="TagAutocomplete"),
#             'journal': HiddenInput
#         }
#
#     def clean(self):
#         cleaned_data = super().clean()
#         # Check if there is not yet another entry for this week.
#         date = cleaned_data["date"]
#         # # first/last day of that week
#         first_day = date - datetime.timedelta(days=date.weekday())
#         last_day = first_day + datetime.timedelta(days=7)
#         other = cleaned_data["journal"].week_entries.filter(
#             date__range=(first_day, last_day)).exclude(pk=self.instance.pk)
#         if other.exists():
#             raise ValidationError("There is already an entry for this week: {}".format(other))
#
#     helper = FormHelper()
#     helper.layout = Layout(
#         Row(
#             Field('date', wrapper_class="col-md-6"),
#         ),
#         Field('focus', autofocus='True'),
#         Field('content', rows="20"),
#         Field('tags'),
#         SaveButton(),
#         CancelButton(),
#     )
