from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Field
from django import forms

from colegend.core.fields import DateFormField
from .models import Journal


class JournalForm(forms.ModelForm):
    class Meta:
        model = Journal
        fields = [
            'spellchecker',
            'day_template',
            'week_template',
            'month_template',
            'quarter_template',
            'year_template',
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Field('spellchecker'),
            Field('day_template', required=False),
            Field('week_template', required=False),
            Field('month_template', required=False),
            Field('quarter_template', required=False),
            Field('year_template', required=False),
        )
        self.helper.add_input(Submit('save', 'Save'))
        self.helper.attrs = {'novalidate': True}


class DatePickerForm(forms.Form):
    date = DateFormField(
        # required = True,
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Field('date', min_width=100),
        )
        self.helper.add_input(Submit('get', 'Go'))

        self.helper.form_class = 'datepicker-form form-inline'
        self.helper.form_show_labels = False
        self.helper.form_method = 'get'
        # self.helper.include_media = False
