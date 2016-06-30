from collections import OrderedDict

from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Sum
from django.utils import timezone
from django.views.generic import TemplateView

from colegend.checkpoints.models import Checkpoint
from colegend.core.templatetags.core_tags import link
from colegend.core.views import RolesRequiredMixin
from colegend.donations.models import Donation
from colegend.roles.models import Role


class MetricsIndexView(LoginRequiredMixin, RolesRequiredMixin, TemplateView):
    template_name = 'metrics/index.html'
    required_roles = ['Core Manager']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        metrics = OrderedDict()

        metrics['date'] = timezone.now()

        legends = get_user_model().objects.count()
        metrics['legends'] = legends

        metrics['donations'] = '€{}'.format(Donation.objects.aggregate(Sum('amount')).get('amount__sum'))

        metrics['total income/outcome'] = link('google docs file', url='https://drive.google.com/drive/u/0/folders/0B2HIrbU2jVlWUjNCZWJMVVhmb2s', external=True)

        guide_checkpoint = Checkpoint.objects.filter(name='cloud guide').first()
        if guide_checkpoint:
            guided_legends = get_user_model().objects.exclude(checkpoints__in=[guide_checkpoint.id]).distinct().count()
        else:
            guided_legends = 'unknown'
        metrics['unguided legends'] = guided_legends

        metrics['facebook likes'] = link('facebook insights', url='https://www.facebook.com/colegend.org/insights/', external=True)

        metrics['partners'] = get_user_model().objects.filter(roles__isnull=False).distinct().count()

        metrics['roles'] = Role.objects.count()

        metrics['filled roles'] = Role.objects.filter(user__isnull=False).distinct().count()

        metrics['unfilled roles'] = Role.objects.filter(user__isnull=True).distinct().count()

        context['metrics'] = metrics
        return context
