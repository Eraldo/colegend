from django.core.urlresolvers import reverse_lazy
from django.shortcuts import redirect
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from lib.views import ActiveUserRequiredMixin, ManagerRequiredMixin
from quotes.forms import QuoteForm
from quotes.models import Quote


class QuoteMixin(ActiveUserRequiredMixin):
    model = Quote
    form_class = QuoteForm
    icon = "quote"
    tutorial = "Quotes"

    def get_queryset(self):
        return super().get_queryset().owned_by(self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class QuoteCreateView(QuoteMixin, CreateView):
    success_url = reverse_lazy('quotes:quote_list')

    def form_valid(self, form):
        user = self.request.user
        form.instance.provider = user
        return super(QuoteCreateView, self).form_valid(form)


class QuoteListView(QuoteMixin, ListView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        quotes = self.get_queryset()
        context['quotes'] = quotes.accepted().order_by('category')
        context['pending'] = quotes.pending()
        context['total_counter'] = Quote.objects.accepted().count()
        context['share_counter'] = self.request.user.quote_set.count()
        context['random_quote'] = Quote.objects.accepted().random()
        return context


class QuoteManageView(ManagerRequiredMixin, QuoteMixin, ListView):
    template_name = "quotes/quote_manage.html"

    def get_queryset(self):
        return Quote.objects.pending().order_by('provider')

    def post(self, request, *args, **kwargs):
        if "accept" in self.request.POST:
            value = self.request.POST.get("accept")
            if value == "all":
                quotes = self.get_queryset()
                for quote in quotes:
                    quote.accept()
            elif value.isdigit():
                pk = int(value)
                Quote.objects.get(pk=pk).accept()
                return redirect("quotes:quote_manage")
        return redirect("quotes:quote_list")


class QuoteShowView(QuoteMixin, DetailView):
    template_name = "quotes/quote_show.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        quote = self.get_object()
        context['owned'] = self.get_object().provider == user
        can_edit = quote.pending() and user.is_manager
        context['controls'] = context['owned'] or can_edit
        return context

    def post(self, request, *args, **kwargs):
        if "accept" in self.request.POST:
            self.get_object().accept()
        return redirect("quotes:quote_list")


class QuoteEditView(QuoteMixin, UpdateView):
    success_url = reverse_lazy('quotes:quote_list')


class QuoteDeleteView(QuoteMixin, DeleteView):
    template_name = "confirm_delete.html"
    success_url = reverse_lazy('quotes:quote_list')
