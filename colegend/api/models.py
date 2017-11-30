from graphene import relay, Int


class CountableConnectionBase(relay.Connection):
    class Meta:
        abstract = True

    total_count = Int()

    def resolve_total_count(self, info, **kwargs):
        return self.iterable.count()
