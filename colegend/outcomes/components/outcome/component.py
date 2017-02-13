from colegend.components.models import Component
from colegend.outcomes.forms import OutcomeStatusForm
from colegend.outcomes.models import Outcome


class OutcomeComponent(Component):
    def get_context(self, context, outcome=None, **kwargs):
        outcome = outcome or context.get('outcome', {})
        request = context.get('request')
        if outcome:
            if isinstance(outcome, Outcome):
                context.update({
                    'id': outcome.id,
                    'name': outcome.name,
                    'description': outcome.description,
                    'status': outcome.status,
                    'inbox': outcome.inbox,
                    'review': outcome.review,
                    'date': outcome.date or '',
                    'deadline': outcome.deadline or '',
                    'estimate': outcome.estimate or '',
                    'url': outcome.detail_url,
                    'status_form': OutcomeStatusForm(instance=outcome, request=request),
                    'actions': [
                        {
                            'name': 'update',
                            'url': outcome.update_url,
                        },
                        {
                            'name': 'delete',
                            'url': outcome.delete_url,
                        },
                    ],
                })
            elif isinstance(outcome, dict):
                context.update(outcome)
        context.update(kwargs)
        return context
