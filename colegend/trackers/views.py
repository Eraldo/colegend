from django.core.urlresolvers import reverse_lazy
from django.utils import timezone
from django.views.generic import TemplateView, CreateView, ListView, UpdateView, DetailView, DeleteView
from django.views.generic.detail import SingleObjectMixin
from django.views.generic.edit import FormMixin
from categories.models import Category
from lib.views import OwnedItemsMixin, ActiveUserRequiredMixin
from trackers.forms import WeightForm, SexForm, BookForm, JokeForm, TransactionForm, DreamForm, SleepForm, WalkForm, \
    TrackerForm, CheckDataForm, NumberDataForm, RatingDataForm
from trackers.models import Book, Sex, Joke, Weight, Transaction, Dream, Sleep, Walk, Tracker


class TrackerMixin(ActiveUserRequiredMixin, OwnedItemsMixin):
    model = Tracker
    icon = "tracker"
    tutorial = "Trackers"


class TrackerListView(TrackerMixin, TemplateView):
    template_name = "trackers/tracker_list.html"


class TrackerNewView(TrackerMixin, CreateView):
    template_name = "trackers/tracker_form.html"
    form_class = TrackerForm

    def form_valid(self, form):
        user = self.request.user
        form.instance.owner = user
        return super().form_valid(form)


class TrackerShowView(TrackerMixin, FormMixin, SingleObjectMixin, ListView):
    template_name = "trackers/tracker_show.html"
    paginate_by = 10

    def set_object_and_object_list(self):
        self.object = self.get_object(queryset=Tracker.objects.owned_by(self.request.user))
        self.object_list = self.get_queryset()

    def get(self, request, *args, **kwargs):
        self.set_object_and_object_list()
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.set_object_and_object_list()
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def get_queryset(self):
        return self.object.data

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tracker = self.object
        context['tracker'] = tracker
        context["type"] = tracker.get_tracker_type_display()
        context["form"] = self.get_form_class()(self.request.POST or None)
        return context

    def get_form_class(self):
        tracker_type = self.object.tracker_type
        if tracker_type == Tracker.CHECK:
            return CheckDataForm
        if tracker_type == Tracker.NUMBER:
            return NumberDataForm
        if tracker_type == Tracker.RATING:
            return RatingDataForm

    def form_valid(self, form):
        tracker = self.object
        form.instance.tracker = tracker
        data_class = type(form.instance)
        data = form.cleaned_data
        date = data.pop("date")
        data_class.objects.update_or_create(tracker=tracker, date=date, defaults=data)
        return super().form_valid(form)

    def get_success_url(self):
        return self.object.get_show_url()


class TrackerEditView(TrackerMixin, UpdateView):
    template_name = "trackers/tracker_form.html"
    form_class = TrackerForm


class TrackerDeleteView(TrackerMixin, DeleteView):
    success_url = reverse_lazy("trackers:tracker_list")
    template_name = "confirm_delete.html"


class DataDeleteView(TrackerMixin, DeleteView):
    success_url = reverse_lazy("trackers:tracker_list")
    template_name = "confirm_delete.html"

    def get_tracker(self):
        tracker_pk = self.kwargs.get("tracker_pk", None)
        if tracker_pk:
            return self.request.user.tracker_set.get(pk=tracker_pk)

    def get_success_url(self):
        tracker = self.get_tracker()
        return tracker.get_show_url()

    def get_object(self, queryset=None):
        pk = self.kwargs.get("pk", None)
        if pk:
            tracker = self.get_tracker()
            if tracker:
                return tracker.data.get(pk=pk)


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
        context["category"] = Category.objects.get(pk=1)
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


class WeightChartView(WeightMixin, ListView):
    template_name = "trackers/weight_chart.html"


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
        context["category"] = Category.objects.get(pk=2)
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


class SexChartView(SexMixin, ListView):
    template_name = "trackers/sex_chart.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            year = int(self.request.GET.get("year"))
        except (ValueError, TypeError):
                year = timezone.now().year
        context["data_list"] = self.get_queryset().filter(date__year=year)
        context["year"] = year
        return context


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
        context["category"] = Category.objects.get(pk=6)
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
        context["category"] = Category.objects.get(pk=5)
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
        context["category"] = Category.objects.get(pk=3)
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


class TransactionChartView(TransactionMixin, ListView):
    template_name = "trackers/transaction_chart.html"
    year = None
    month = None

    def get_queryset(self):
        try:
            year = int(self.request.GET.get("year"))
            month = int(self.request.GET.get("month"))
        except (ValueError, TypeError):
                year = timezone.now().year
                month = timezone.now().month
        self.year = year
        self.month = month
        queryset = super().get_queryset().filter(time__year=year, time__month=month).order_by("time")
        cumulative = 0
        for item in queryset:
            cumulative += item.value
            item.cumulative = cumulative
        self.balance = cumulative
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["year"] = self.year
        context["month"] = self.month
        context["balance"] = self.balance
        return context


class DreamMixin(TrackerMixin):
    success_url = reverse_lazy("trackers:dream_list")
    model = Dream
    form_class = DreamForm


class DreamListView(DreamMixin, ListView):
    success_url = reverse_lazy("trackers:tracker_list")
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["total_counter"] = self.get_queryset().count()
        context["category"] = Category.objects.get(pk=7)
        return context


class DreamNewView(DreamMixin, CreateView):
    template_name = "trackers/tracker_form.html"

    def form_valid(self, form):
        user = self.request.user
        form.instance.owner = user
        return super().form_valid(form)


class DreamShowView(DreamMixin, DetailView):
    template_name = "trackers/tracker_show.html"


class DreamEditView(DreamMixin, UpdateView):
    template_name = "trackers/tracker_form.html"


class DreamDeleteView(DreamMixin, DeleteView):
    template_name = "confirm_delete.html"


class DreamChartView(DreamMixin, ListView):
    template_name = "trackers/dream_chart.html"
    year = None

    def get_queryset(self):
        queryset = super().get_queryset()
        try:
            year = int(self.request.GET.get("year"))
        except (ValueError, TypeError):
            year = timezone.now().year
        self.year = year
        return queryset.filter(date__year=year)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["year"] = self.year
        return context


class SleepMixin(TrackerMixin):
    success_url = reverse_lazy("trackers:sleep_list")
    model = Sleep
    form_class = SleepForm


class SleepListView(SleepMixin, ListView):
    success_url = reverse_lazy("trackers:tracker_list")
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["total_counter"] = self.get_queryset().count()
        context["category"] = Category.objects.get(pk=1)
        return context


class SleepNewView(SleepMixin, CreateView):
    template_name = "trackers/tracker_form.html"

    def form_valid(self, form):
        user = self.request.user
        form.instance.owner = user
        return super().form_valid(form)


class SleepShowView(SleepMixin, DetailView):
    template_name = "trackers/tracker_show.html"


class SleepEditView(SleepMixin, UpdateView):
    template_name = "trackers/tracker_form.html"


class SleepDeleteView(SleepMixin, DeleteView):
    template_name = "confirm_delete.html"


class SleepChartView(SleepMixin, ListView):
    template_name = "trackers/sleep_chart.html"


class WalkMixin(TrackerMixin):
    success_url = reverse_lazy("trackers:walk_list")
    model = Walk
    form_class = WalkForm


class WalkListView(WalkMixin, ListView):
    success_url = reverse_lazy("trackers:tracker_list")
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["total_counter"] = self.get_queryset().count()
        context["category"] = Category.objects.get(pk=4)
        return context


class WalkNewView(WalkMixin, CreateView):
    template_name = "trackers/tracker_form.html"

    def form_valid(self, form):
        user = self.request.user
        form.instance.owner = user
        return super().form_valid(form)


class WalkShowView(WalkMixin, DetailView):
    template_name = "trackers/tracker_show.html"


class WalkEditView(WalkMixin, UpdateView):
    template_name = "trackers/tracker_form.html"


class WalkDeleteView(WalkMixin, DeleteView):
    template_name = "confirm_delete.html"


class WalkChartView(WalkMixin, ListView):
    template_name = "trackers/walk_chart.html"
    year = None

    def get_queryset(self):
        queryset = super().get_queryset()
        try:
            year = int(self.request.GET.get("year"))
        except (ValueError, TypeError):
            year = timezone.now().year
        self.year = year
        return queryset.filter(start__year=year)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["year"] = self.year
        return context
