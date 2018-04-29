from django import template


register = template.Library()


@register.simple_tag
def get_scoped_focus(user, scope):
    from colegend.office.models import Focus
    try:
        focus = user.focuses.get(scope=scope.name, start=scope.start)
    except Focus.DoesNotExist:
        focus = Focus.objects.none()
    return focus


@register.simple_tag
def get_done_steps(outcome, scope):
    if scope:
        return outcome.steps.filter(completed_at__date__range=(scope.start, scope.end))
    else:
        return outcome.steps


@register.simple_tag
def get_outcome_status(outcome, scope):
    """
    Success: Outcome done or at least one step done.
    Neutral: Has a next steps defined.
    Fail: No next step defined.
    :return:
    """
    if outcome.is_inactive:
        return '[✔]'
    # Is there a completed step for this scope?
    if outcome.steps.filter(completed_at__date__range=(scope.start, scope.end)).exists():
        return '[✔]'
    # Is there a next step?
    if outcome.next_step:
        return '[ ]'
    else:
        return '[✖]'
