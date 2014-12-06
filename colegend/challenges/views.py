from django.core.exceptions import PermissionDenied
from django.core.urlresolvers import reverse_lazy
from django.template.loader import render_to_string
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView
from challenges.forms import ChallengeForm
from challenges.models import Challenge
from lib.views import ActiveUserRequiredMixin

__author__ = 'eraldo'


class ChallengeMixin(ActiveUserRequiredMixin):
    model = Challenge
    form_class = ChallengeForm
    icon = "challenge"
    tutorial = "Challenges"

    def get_queryset(self):
        qs = super(ChallengeMixin, self).get_queryset()
        return qs.filter(accepted=True)


class ChallengeListView(ChallengeMixin, ListView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["contribution_counter"] = Challenge.objects.filter(provider=self.request.user).count()
        return context


class ChallengeCreateView(ChallengeMixin, CreateView):
    success_url = reverse_lazy('challenges:challenge_list')

    def form_valid(self, form):
        user = self.request.user
        form.instance.provider = user
        return super(ChallengeCreateView, self).form_valid(form)

    def get_initial(self):
        initial = super().get_initial()
        template = render_to_string("challenges/challenge.md")
        initial['content'] = template
        return initial


class ChallengeShowView(ChallengeMixin, DetailView):
    template_name = "challenges/challenge_show.html"


class ChallengeEditView(ChallengeMixin, UpdateView):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_superuser or request.user == self.get_object().provider:
            return super(ChallengeEditView, self).dispatch(request, *args, **kwargs)
        else:
            raise PermissionDenied


class ChallengeDeleteView(ChallengeMixin, DeleteView):
    template_name = "confirm_delete.html"
    success_url = reverse_lazy('challenges:challenge_list')
