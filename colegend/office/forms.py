from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Field
from django import forms

from colegend.office.models import Focus
from colegend.outcomes.fields import OutcomeCreateFormField


class FocusForm(forms.ModelForm):
    class Meta:
        model = Focus
        fields = [
            'owner',
            'scope',
            'start',
            'outcome_1',
            'outcome_2',
            'outcome_3',
            'outcome_4',
        ]

    def __init__(self, *args, **kwargs):
        owner = kwargs.pop('owner', None)
        queryset = owner.outcomes.all()
        super().__init__(*args, **kwargs)

        # Update the outcomes field to use the custom django-autocomplete's create field
        self.fields['outcome_1'] = OutcomeCreateFormField(queryset, required=False)
        self.fields['outcome_2'] = OutcomeCreateFormField(queryset, required=False)
        self.fields['outcome_3'] = OutcomeCreateFormField(queryset, required=False)
        self.fields['outcome_4'] = OutcomeCreateFormField(queryset, required=False)

        self.helper = FormHelper()
        self.helper.layout = Layout(
            Field('owner', type='hidden'),
            Field('scope', type='hidden'),
            Field('start', type='hidden'),
            Field('outcome_1'),
            Field('outcome_2'),
            Field('outcome_3'),
            Field('outcome_4'),
        )
        self.helper.add_input(Submit('save', 'Save'))
        self.helper.include_media = False
        self.helper.form_show_labels = False

    def clean(self):
        outcome_1 = self.cleaned_data.get('outcome_1')
        outcome_2 = self.cleaned_data.get('outcome_2')
        outcome_3 = self.cleaned_data.get('outcome_3')
        outcome_4 = self.cleaned_data.get('outcome_4')
        outcomes = [outcome_1, outcome_2, outcome_3, outcome_4]
        outcomes = [outcome for outcome in outcomes if outcome]
        if len(outcomes) != len(set(outcomes)):
            message = 'Please chose an ontcome only once.'
            self.add_error(None, message)
        return super().clean()
#
#
# class ScopePickerForm(forms.Form):
#     scope = forms.ChoiceField(
#         choices=SCOPE_CHOICES,
#     )
#
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.helper = FormHelper()
#         self.helper.layout = Layout(
#             Field('scope'),
#         )
#         self.helper.add_input(Submit('get', 'Go'))
#         self.helper.form_class = 'form-inline'
#         self.helper.form_show_labels = False
#         self.helper.form_method = 'get'
#         # self.helper.include_media = False
