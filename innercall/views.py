from braces.views import LoginRequiredMixin
from django.shortcuts import redirect
from django.views.generic import CreateView, UpdateView

from .models import InnerCall
from .forms import InnerCallForm


class InnerCallCreateView(LoginRequiredMixin, CreateView):
    template_name = 'innercall/update.html'
    model = InnerCall
    form_class = InnerCallForm

    def get(self, request, *args, **kwargs):
        # redirect if the user already owns one
        user = self.request.user
        try:
            return redirect(user.innercall)
        except InnerCall.DoesNotExist:
            return super().get(request, *args, **kwargs)

    def get_initial(self):
        initial = super().get_initial()
        initial['owner'] = self.request.user
        return initial

    def form_valid(self, form):
        conscious = self.request.user.conscious
        conscious.inner_call = True
        conscious.save()
        return super().form_valid(form)


class InnerCallUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'innercall/update.html'
    model = InnerCall
    form_class = InnerCallForm

    def get_object(self, queryset=None):
        user = self.request.user
        return user.innercall
