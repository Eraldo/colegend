# Import the reverse lookup function
from braces.views import LoginRequiredMixin
from django.core.urlresolvers import reverse, reverse_lazy

# view imports
from django.shortcuts import redirect
from django.views.generic import DetailView, TemplateView
from django.views.generic import RedirectView
from django.views.generic import UpdateView
from django.views.generic import ListView

# Only authenticated users can access views using this.
from lib.views import ActiveUserRequiredMixin

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
        return Settings.objects.get(owner=self.request.user)
        # slug_field = "owner"
        # slug_url_kwarg = "owner"
