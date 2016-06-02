from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib import messages
from django.shortcuts import redirect
from django.views.generic import UpdateView, CreateView
from django.utils.translation import ugettext as _

from colegend.games.views import complete_card

from .models import Biography
from .forms import BiographyForm


class BiographyCreateView(LoginRequiredMixin, CreateView):
    template_name = 'biography/update.html'
    model = Biography
    form_class = BiographyForm

    def get(self, request, *args, **kwargs):
        # redirect if the user already owns one
        user = self.request.user
        try:
            return redirect(user.biography)
        except Biography.DoesNotExist:
            return super().get(request, *args, **kwargs)

    def get_initial(self):
        initial = super().get_initial()
        initial['owner'] = self.request.user
        return initial

    def form_valid(self, form):
        user = self.request.user
        # update the game
        complete_card(self.request, 'biography')
        return super().form_valid(form)


class BiographyUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'biography/update.html'
    model = Biography
    form_class = BiographyForm

    def get_object(self, queryset=None):
        user = self.request.user
        return user.biography

    def form_valid(self, form):
        message = _('changes saved')
        messages.success(self.request, message)
        return super().form_valid(form)
