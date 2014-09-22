from django.views.generic import TemplateView
from quotes.models import Quote


class RandomQuoteView(TemplateView):
    template_name = "quotes/random.html"

    def get_context_data(self, **kwargs):
        context = super(RandomQuoteView, self).get_context_data(**kwargs)
        try:
            quote = Quote.objects.order_by('?')[0]
        except Quote.DoesNotExist:
            quote = None
        context['quote'] = quote
        return context
