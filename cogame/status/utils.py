from status.models import Status

__author__ = 'eraldo'


class StatusQueryMixin:
    """
    A set of methods for filtering a model with a Status field by status.
    """
    def open(self):
        return self.filter(status__type=Status.OPEN)

    def closed(self):
        return self.filter(status__type=Status.CLOSED)

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
