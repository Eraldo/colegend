from django import template
from django.utils import timezone

register = template.Library()


@register.simple_tag
def get_done_steps(outcome, start, end):
    if start and end:
        return outcome.steps.filter(completed_at__date__range=(start, end))
    else:
        return outcome.steps


# @register.simple_tag
# def get_outcome_status(outcome, start, end):
#     """
#     Success: Outcome done or at least one step done.
#     Neutral: Has a next steps defined.
#     Fail: No next step defined.
#     :return:
#     """
#     if outcome.is_inactive:
#         return '[x]'
#     # Is there a completed step for this scope?
#     if outcome.steps.filter(completed_at__range=(start, end)).exists():
#         return '[x]'
#     # Is there a next step?
#     if outcome.next_step:
#         return '[ ]'
#     else:
#         return '[-]'
