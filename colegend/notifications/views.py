from django.shortcuts import redirect
from lib.views import ActiveUserRequiredMixin, ManagerRequiredMixin
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from lib.views import OwnedItemsMixin
from notifications.forms import NotificationForm
from notifications.models import Notification

__author__ = 'eraldo'


class NotificationMixin(ActiveUserRequiredMixin, OwnedItemsMixin):
    model = Notification
    form_class = NotificationForm
    icon = "notification"
    tutorial = "Notifications"


class NotificationListView(NotificationMixin, ListView):
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_counter'] = self.get_queryset().count()
        return context

    def post(self, request):
        action = request.POST.get("action")
        if action and action == "mark_all_as_read":
            self.get_queryset().mark_as_read()
        return redirect(".")


class NotificationNewView(ManagerRequiredMixin, NotificationMixin, CreateView):
    success_url = reverse_lazy('notifications:notification_list')

    def form_valid(self, form):
        user = self.request.user
        form.instance.owner = user
        return super(NotificationNewView, self).form_valid(form)


class NotificationShowView(NotificationMixin, DetailView):
    template_name = "notifications/notification_show.html"

    def get(self, request, *args, **kwargs):
        notification = self.get_object()
        notification.read = True
        notification.save()
        return super().get(request, *args, **kwargs)


class NotificationEditView(NotificationMixin, UpdateView):
    success_url = reverse_lazy('notifications:notification_list')


class NotificationDeleteView(NotificationMixin, DeleteView):
    template_name = "confirm_delete.html"
    success_url = reverse_lazy('notifications:notification_list')
