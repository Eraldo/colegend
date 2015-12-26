from braces.views import LoginRequiredMixin
from django.shortcuts import redirect
from django.views.generic import UpdateView, CreateView
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
        conscious = self.request.user.conscious
        conscious.outer_call = True
        conscious.save()
        return super().form_valid(form)


class OuterCallUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'outercall/update.html'
    model = OuterCall
    form_class = OuterCallForm

    def get_object(self, queryset=None):
        user = self.request.user
        return user.outercall
