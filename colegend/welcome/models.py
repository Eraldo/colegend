from allauth.account.utils import perform_login
from django.conf import settings
from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse
from wagtail.wagtailcore.models import Page

from colegend.users.models import User
from colegend.welcome.forms import WelcomeEmailForm, WelcomePasswordForm


class WelcomePage(Page):
    template = 'welcome/base.html'

    parent_page_types = ['cms.RootPage']
    subpage_types = []

    email = ''
    name = ''
    password = ''
    user = None

    def serve(self, request, *args, **kwargs):
        email = request.POST.get('email')
        if email:
            self.email = email
            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                user = User.objects.none()
            if user:
                self.name = user.name
                self.email = user.email
                password = request.POST.get('password')
                if password:
                    self.password = password
                    if user.check_password(password):
                        return perform_login(request, user, email_verification=settings.ACCOUNT_EMAIL_VERIFICATION)
                    else:
                        messages.error(request, 'Something did not match. Please try again!')
            else:
                signup_url = reverse('account_signup') + '?email=' + email
                return redirect(signup_url)
        return super().serve(request, *args, **kwargs)

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        if settings.ACCOUNT_ALLOW_REGISTRATION:
            context['open'] = True
            context['name'] = self.name
            if not self.email:
                context['form'] = WelcomeEmailForm()
            else:
                data = {'email': self.email, 'password': self.password}
                if self.password:
                    context['form'] = WelcomePasswordForm(data)
                else:
                    context['form'] = WelcomePasswordForm(initial=data)
        return context
