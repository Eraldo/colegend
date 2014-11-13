# Import the reverse lookup function
from braces.views import LoginRequiredMixin
from django.contrib import messages
from django.core.urlresolvers import reverse, reverse_lazy

# view imports
from django.shortcuts import redirect
from django.views.generic import DetailView, TemplateView
from django.views.generic import RedirectView
from django.views.generic import UpdateView
from django.views.generic import ListView

# Only authenticated users can access views using this.
from lib.views import ActiveUserRequiredMixin, ManagerRequiredMixin

# Import the form from users/forms.py
from .forms import UserForm, SettingsForm

# Import the customized User model
from .models import User, Settings


class UserMixin(ActiveUserRequiredMixin):
    def get_queryset(self):
        return super(UserMixin, self).get_queryset().accepted()


class UserInactiveView(LoginRequiredMixin, TemplateView):
    template_name = "users/inactive.html"

    def get(self, request, *args, **kwargs):
        if request.user.is_accepted:
            return redirect("home")
        return super(UserInactiveView, self).get(request, *args, **kwargs)


class UserDetailView(UserMixin, DetailView):
    model = User
    # These next two lines tell the view to index lookups by username
    slug_field = "username"
    slug_url_kwarg = "username"


class UserRedirectView(UserMixin, RedirectView):
    permanent = False

    def get_redirect_url(self):
        return reverse("users:detail",
                       kwargs={"username": self.request.user.username})


class UserUpdateView(UserMixin, UpdateView):
    form_class = UserForm

    # we already imported User in the view code above, remember?
    model = User

    # send the user back to their own page after a successful update
    def get_success_url(self):
        return reverse("users:detail",
                       kwargs={"username": self.request.user.username})

    def get_object(self):
        # Only get the User record for the user making the request
        return User.objects.get(username=self.request.user.username)


class UserListView(UserMixin, ListView):
    model = User
    # These next two lines tell the view to index lookups by username
    slug_field = "username"
    slug_url_kwarg = "username"


class SettingsUpdateView(UserMixin, UpdateView):
    model = Settings
    form_class = SettingsForm

    def get_success_url(self):
        return reverse("users:detail",
                       kwargs={"username": self.request.user.username})

    def get_object(self):
        return self.request.user.settings
        # slug_field = "owner"
        # slug_url_kwarg = "owner"


class UserManageListView(ManagerRequiredMixin, ListView):
    model = User
    template_name = "users/user_manage.html"

    def get_queryset(self):
        return super().get_queryset().pending()


class UserManageDetailView(ManagerRequiredMixin, DetailView):
    model = User
    template_name = "users/user_manage_detail.html"
    # These next two lines tell the view to index lookups by username
    slug_field = "username"
    slug_url_kwarg = "username"

    def get_queryset(self):
        return super().get_queryset().pending()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.get_object()
        context['name'] = user.first_name
        context['pronoun'] = "him" if user.contact.gender == 'M' else "her"
        context['profile'] = user.profile
        context['contact'] = user.contact
        return context

    def post(self, request, *args, **kwargs):
        verify = request.POST.get("verify")
        user = self.get_object()
        if user.pk == int(verify):
            user.accept(accepter=self.request.user)
            message = '{} is now verified.'.format(user)
            messages.add_message(request, messages.SUCCESS, message)
        return redirect("users:manage")
