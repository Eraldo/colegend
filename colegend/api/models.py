from graphene import relay, Int
from graphene_django.filter import DjangoFilterConnectionField


class CountableConnectionBase(relay.Connection):
    class Meta:
        abstract = True

    total_count = Int()

    def resolve_total_count(self, info, **kwargs):
        return self.iterable.count()


class DjangoUserFilterConnectionField(DjangoFilterConnectionField):
    """
    Workaround to make resolver work with DjangoFilterConnectionField

    See also: https://github.com/graphql-python/graphene-django/issues/30
    """
    @classmethod
    def connection_resolver(cls, resolver, connection, default_manager, max_limit,
                            enforce_first_or_last, filterset_class, filtering_args,
                            root, info, **args):
        filter_kwargs = {k: v for k, v in args.items() if k in filtering_args}
        qs = filterset_class(
            data=filter_kwargs,
            queryset=default_manager.get_queryset(),
            user=info.context.user
        ).qs

        return super(DjangoFilterConnectionField, cls).connection_resolver(
            resolver,
            connection,
            qs,
            max_limit,
            enforce_first_or_last,
            root,
            info,
            **args
        )
