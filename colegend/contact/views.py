from django.contrib import messages
from django.contrib.auth import get_user_model
from django.views.generic import FormView
from contact.forms import ContactForm, PublicContactForm
from lib.views import get_icon

__author__ = "Eraldo Helal"


class ContactView(FormView):
    template_name = "contact/contact.html"
    form_class = ContactForm
    success_url = '.'

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
        context = super(ContactView, self).get_context_data(**kwargs)
        user_model = get_user_model()
        try:
            eraldo = user_model.objects.get(username="Eraldo")
        except user_model.DoesNotExist:
            eraldo = None
        context['eraldo'] = eraldo
        context["icon"] = get_icon("envelope")
        return context
