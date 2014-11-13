from django.core.urlresolvers import reverse_lazy
from django.shortcuts import redirect
from django.views.generic import TemplateView, CreateView, ListView, DetailView, UpdateView, DeleteView
from lib.views import ActiveUserRequiredMixin, ManagerRequiredMixin
from quotes.forms import QuoteForm
from quotes.models import Quote


class QuoteMixin(ActiveUserRequiredMixin):
    model = Quote
    form_class = QuoteForm

    def get_queryset(self):
        return super().get_queryset().owned_by(self.request.user)


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
        context['quotes'] = quotes.accepted()
        context['pending'] = quotes.pending()
        context['contribution_counter'] = quotes.count()
        context['random_quote'] = Quote.objects.accepted().random()
        return context


class QuoteManageView(ManagerRequiredMixin, ListView):
    template_name = "quotes/quote_manage.html"
    model = Quote

    def get_queryset(self):
        return super().get_queryset().pending()


class QuoteShowView(DetailView):
    template_name = "quotes/quote_show.html"
    model = Quote

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
    success_url = reverse_lazy('quotes:quote_list')