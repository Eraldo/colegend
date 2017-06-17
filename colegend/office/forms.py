from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Field
from django import forms
from django.utils.translation import ugettext_lazy as _

from colegend.office.models import Focus, DAY, WEEK, MONTH
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
        super().__init__(*args, **kwargs)

        queryset = owner.outcomes.all()
        instance = kwargs.get('instance', None)

        # Update the outcomes field to use the custom django-autocomplete's create field
        self.fields['outcome_1'] = OutcomeCreateFormField(queryset, required=False)
        self.fields['outcome_2'] = OutcomeCreateFormField(queryset, required=False)
        self.fields['outcome_3'] = OutcomeCreateFormField(queryset, required=False)
        self.fields['outcome_4'] = OutcomeCreateFormField(queryset, required=False)

        if instance:
            self.fields['update_reason'] = forms.CharField(widget=forms.Textarea, required=True)

        self.helper = FormHelper()
        self.helper.layout = Layout(
            Field('owner', type='hidden'),
            Field('scope', type='hidden'),
            Field('start', type='hidden'),
            Field('outcome_1'),
            Field('outcome_2'),
            Field('outcome_3'),
            Field('outcome_4'),
            Field('update_reason', placeholder=_("Reason for my update..."), rows=2),
        )
        self.helper.add_input(Submit('save', 'Save'))
        # self.helper.add_input(Submit('cancel', 'Cancel', css_class='btn-secondary'))
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

    def save(self, commit=True):
        # Checking if an outcome field was changed.
        changed_outcome_fields = [field for field in self.changed_data if field.startswith('outcome')]
        if changed_outcome_fields:
            initial = self.initial
            instance = self.instance
            owner = instance.owner
            update_reason = self.cleaned_data.get('update_reason')

            # Creating update message
            action = _('updated') if update_reason else _('set')
            subject = '{user} {action} {possessive_pronoun} {scope} focus: ({scope_display})'.format(
                user=owner,
                action=action,
                possessive_pronoun=owner.get_pronoun(kind='possessive adjective'),
                scope=instance.scope,
                scope_display=instance.get_scope(),
            )
            message = subject + '\n\n'
            for field in changed_outcome_fields:
                title = field.title().replace('_', ' ')
                old_id = initial.get(field)
                if old_id:
                    old_outcome = owner.outcomes.get(id=old_id)
                else:
                    old_outcome = '---'
                new_outcome = getattr(instance, field) or '---'
                if update_reason:
                    message += '{title}: {old} => {new}\n'.format(title=title, old=old_outcome, new=new_outcome)
                else:
                    message += '{title}: {new}\n'.format(title=title, new=new_outcome)
            if update_reason:
                message += '\nUpdate Reason:\n{reason}'.format(reason=update_reason)

            # Notifying partners
            if instance.scope == DAY:
                group = owner.duo
            elif instance.scope == WEEK:
                group = owner.clan
            elif instance.scope == MONTH:
                group = owner.tribe
            if group:
                group.notify_partners(owner, subject, message)

        return super().save(commit)

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
