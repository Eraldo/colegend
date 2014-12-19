from statuses.models import Status

__author__ = 'eraldo'


class StatusFilterMixin:
    status_default = ['open']

    def filter_status(self, queryset):
        """
        Filter querysey by posted status

        :param queryset:
        :return:
        """
        status_filters = self.request.GET.getlist('status', self.status_default)
        for status in status_filters:
            queryset = queryset.status(status)
        return queryset

    def _add_status_to_context(self, context):
        """
        Add the posted status to the context dictionary

        :param context: context dictionary
        """
        status_filters = self.request.GET.getlist('status', self.status_default)
        context['status_filters'] = status_filters

    def get_context_data(self, **kwargs):
        """
        Add the status filters to the context.

        :param kwargs:
        :return: context with added key 'status_filters'
        """
        context = super(StatusFilterMixin, self).get_context_data(**kwargs)
        self._add_status_to_context(context)
        context['status_options'] = Status.objects.all()
        return context


class StatusQueryMixin:
    """
    A set of methods for filtering a model with a Status field by status.
    """
    def open(self):
        return self.filter(status__type=Status.OPEN)

    def closed(self):
        return self.filter(status__type=Status.CLOSED)

    def next(self):
        return self.filter(status__name="next")

    def status(self, status):
        """
        Filters the QuerySet based on a given status.

        :param status: status, status name or status type (open|closed) to filter on
        :return: filtered QuerySet
        """
        if status == "open":
            return self.open()
        elif status == "closed":
            return self.closed()
        return self.filter(status__name=status)
