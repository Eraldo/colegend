from django.core.urlresolvers import reverse_lazy
from django.views.generic import TemplateView, CreateView, ListView, UpdateView, DetailView, DeleteView
from lib.views import OwnedItemsMixin, ActiveUserRequiredMixin
from trackers.forms import WeightForm, SexForm, BookForm, JokeForm, TransactionForm
from trackers.models import Book, Sex, Joke, Weight, Transaction


class TrackerMixin(ActiveUserRequiredMixin, OwnedItemsMixin):
    icon = "tracker"
    tutorial = "Trackers"


class TrackerListView(TrackerMixin, TemplateView):
    template_name = "trackers/tracker_list.html"


class WeightMixin(TrackerMixin):
    success_url = reverse_lazy("trackers:weight_list")
    model = Weight
    form_class = WeightForm


class WeightListView(WeightMixin, ListView):
    success_url = reverse_lazy("trackers:tracker_list")
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["total_counter"] = self.get_queryset().count()
        return context


class WeightNewView(WeightMixin, CreateView):
    template_name = "trackers/tracker_form.html"

    def get_initial(self):
        initial = super().get_initial()
        try:
            initial['weight'] = Weight.objects.owned_by(self.request.user).first().weight
        except (Sex.DoesNotExist, AttributeError):
            pass
        return initial

    def form_valid(self, form):
        user = self.request.user
        form.instance.owner = user
        return super().form_valid(form)


class WeightShowView(WeightMixin, DetailView):
    template_name = "trackers/tracker_show.html"


class WeightEditView(WeightMixin, UpdateView):
    template_name = "trackers/tracker_form.html"


class WeightDeleteView(WeightMixin, DeleteView):
    template_name = "confirm_delete.html"


class SexMixin(TrackerMixin):
    success_url = reverse_lazy("trackers:sex_list")
    model = Sex
    form_class = SexForm


class SexListView(SexMixin, ListView):
    success_url = reverse_lazy("trackers:tracker_list")
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["total_counter"] = self.get_queryset().count()
        return context


class SexNewView(SexMixin, CreateView):
    template_name = "trackers/tracker_form.html"

    def get_initial(self):
        initial = super().get_initial()
        try:
            initial['person'] = Sex.objects.owned_by(self.request.user).first().person
        except (Sex.DoesNotExist, AttributeError):
            pass
        return initial

    def form_valid(self, form):
        user = self.request.user
        form.instance.owner = user
        return super().form_valid(form)


class SexShowView(SexMixin, DetailView):
    template_name = "trackers/tracker_show.html"


class SexEditView(SexMixin, UpdateView):
    template_name = "trackers/tracker_form.html"


class SexDeleteView(SexMixin, DeleteView):
    template_name = "confirm_delete.html"


class BookMixin(TrackerMixin):
    success_url = reverse_lazy("trackers:book_list")
    model = Book
    form_class = BookForm


class BookListView(BookMixin, ListView):
    success_url = reverse_lazy("trackers:tracker_list")
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["total_counter"] = self.get_queryset().count()
        return context


class BookNewView(BookMixin, CreateView):
    template_name = "trackers/tracker_form.html"

    def form_valid(self, form):
        user = self.request.user
        form.instance.owner = user
        return super().form_valid(form)


class BookShowView(BookMixin, DetailView):
    template_name = "trackers/tracker_show.html"


class BookEditView(BookMixin, UpdateView):
    template_name = "trackers/tracker_form.html"


class BookDeleteView(BookMixin, DeleteView):
    template_name = "confirm_delete.html"


class JokeMixin(TrackerMixin):
    success_url = reverse_lazy("trackers:joke_list")
    model = Joke
    form_class = JokeForm


class JokeListView(JokeMixin, ListView):
    success_url = reverse_lazy("trackers:tracker_list")
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["total_counter"] = self.get_queryset().count()
        return context


class JokeNewView(JokeMixin, CreateView):
    template_name = "trackers/tracker_form.html"

    def form_valid(self, form):
        user = self.request.user
        form.instance.owner = user
        return super().form_valid(form)


class JokeShowView(JokeMixin, DetailView):
    template_name = "trackers/tracker_show.html"


class JokeEditView(JokeMixin, UpdateView):
    template_name = "trackers/tracker_form.html"


class JokeDeleteView(JokeMixin, DeleteView):
    template_name = "confirm_delete.html"


class TransactionMixin(TrackerMixin):
    success_url = reverse_lazy("trackers:transaction_list")
    model = Transaction
    form_class = TransactionForm


class TransactionListView(TransactionMixin, ListView):
    success_url = reverse_lazy("trackers:tracker_list")
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["total_counter"] = self.get_queryset().count()
        return context


class TransactionNewView(TransactionMixin, CreateView):
    template_name = "trackers/tracker_form.html"

    def form_valid(self, form):
        user = self.request.user
        form.instance.owner = user
        return super().form_valid(form)


class TransactionShowView(TransactionMixin, DetailView):
    template_name = "trackers/tracker_show.html"


class TransactionEditView(TransactionMixin, UpdateView):
    template_name = "trackers/tracker_form.html"


class TransactionDeleteView(TransactionMixin, DeleteView):
    template_name = "confirm_delete.html"

