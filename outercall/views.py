from braces.views import LoginRequiredMixin
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from django.template.loader import render_to_string
from django.utils.safestring import mark_safe
from django.views.generic import UpdateView, CreateView
from django.utils.translation import ugettext as _

from games.views import complete_card
from .models import OuterCall
from .forms import OuterCallForm


class OuterCallCreateView(LoginRequiredMixin, CreateView):
    template_name = 'outercall/update.html'
    model = OuterCall
    form_class = OuterCallForm

    def get(self, request, *args, **kwargs):
        # redirect if the user already owns one
        user = self.request.user
        try:
            return redirect(user.outercall)
        except OuterCall.DoesNotExist:
            return super().get(request, *args, **kwargs)

    def get_initial(self):
        initial = super().get_initial()
        initial['owner'] = self.request.user
        return initial

    def form_valid(self, form):
        user = self.request.user
        # update the user path
        conscious = user.conscious
        conscious.outer_call = True
        conscious.save()
        # update the game
        complete_card(self.request, 'outer call')
        return super().form_valid(form)


class OuterCallUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'outercall/update.html'
    model = OuterCall
    form_class = OuterCallForm

    def get_object(self, queryset=None):
        user = self.request.user
        return user.outercall

    def form_valid(self, form):
        message = _('changes saved')
        messages.success(self.request, message)
        return super().form_valid(form)
