__author__ = 'eraldo'


class OwnedItemsMixin:
    def get_queryset(self):
        return super(OwnedItemsMixin, self).get_queryset().owned_by(self.request.user)
