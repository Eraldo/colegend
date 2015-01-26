from django.contrib import messages
from django.contrib.auth import get_user_model
from django.core.urlresolvers import reverse_lazy
from django.views.generic import FormView
from contact.forms import ContactForm, PublicContactForm, MessageForm
from lib.views import ActiveUserRequiredMixin

__author__ = "Eraldo Helal"


class ContactView(FormView):
    template_name = "contact/contact.html"
    form_class = ContactForm
    success_url = '.'
    icon = "contact"

    def get_form_class(self):
        if not self.request.user.is_authenticated():
            return PublicContactForm
        return super().get_form_class()

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.send_email(self.request.user)
        messages.success(self.request, 'Your message has been sent.')
        return super(ContactView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        # TODO: Remove hardcoded username from contact view.
        # At the moment the user avatar needs this user.
        context = super(ContactView, self).get_context_data(**kwargs)
        user_model = get_user_model()
        try:
            eraldo = user_model.objects.get(username="Eraldo")
        except user_model.DoesNotExist:
            eraldo = None
        context['eraldo'] = eraldo
        return context


class MessageView(ActiveUserRequiredMixin, FormView):
    template_name = "contact/message.html"
    form_class = MessageForm
    success_url = reverse_lazy('home')
    icon = "contact"

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.send(self.request.user)
        messages.success(self.request, 'Your message has been sent.')
        return super().form_valid(form)
