from random import randint

from allauth.account.utils import perform_login
from django.conf import settings
from django.contrib import messages
from django.db import IntegrityError
from django.shortcuts import redirect
from django.template.response import TemplateResponse
from django.urls import reverse
from django.db import models
from wagtail.contrib.wagtailroutablepage.models import RoutablePageMixin, route
from wagtail.wagtailcore.models import Page

from colegend.core.models import TimeStampedBase
from colegend.users.models import User
from colegend.welcome.forms import WelcomeEmailForm, WelcomePasswordForm


def generate_code():
    return randint(1000, 9999)


class WaitingUser(TimeStampedBase, models.Model):
    email = models.EmailField(
        unique=True
    )
    code = models.PositiveSmallIntegerField(default=generate_code)
    informed = models.BooleanField(default=False)
    accepted = models.BooleanField(default=False)


class WelcomePage(RoutablePageMixin, Page):
    template = 'welcome/base.html'

    parent_page_types = ['cms.RootPage']
    subpage_types = []

    email = ''
    name = ''
    password = ''
    user = None

    @route(r'^$')
    def index(self, request, *args, **kwargs):
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
                # Adding email to waiting list.
                try:
                    WaitingUser.objects.create(email=email)
                except IntegrityError:
                    pass
                next_url = self.url + self.reverse_subpage('waiting_list') + '?email={0}'.format(email)
                return redirect(next_url)
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

    @route(r'^waiting-list/$')
    def waiting_list(self, request):
        email = request.GET.get('email') or request.POST.get('email')
        code = request.POST.get('code')
        if email and code:
            found = False
            try:
                found = WaitingUser.objects.get(email=email, code=int(code))
            except WaitingUser.DoesNotExist:
                pass
            if found:
                found.accepted = True
                found.save()
                next_url = reverse('account_signup') + '?email=' + email
                return redirect(next_url)
            else:
                messages.error(request, 'Attempt failed. Please make sure you use the correct code.')
        return TemplateResponse(
            request,
            'welcome/waiting_list.html',
            {'email': email}
        )
