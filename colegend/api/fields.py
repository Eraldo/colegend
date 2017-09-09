from functools import partial

from graphene import Field, List
from graphene_django.filter.utils import (
    get_filtering_args_from_filterset,
    get_filterset_class
)


class DjangoFilterField(Field):

    def __init__(self, _type, fields=None, extra_filter_meta=None,
                 filterset_class=None, *args, **kwargs):

        _fields = _type._meta.filter_fields
        _model = _type._meta.model

        self.fields = fields or _fields
        meta = dict(model=_model, fields=self.fields)
        if extra_filter_meta:
            meta.update(extra_filter_meta)
        self.filterset_class = get_filterset_class(filterset_class, **meta)
        self.filtering_args = get_filtering_args_from_filterset(self.filterset_class, _type)
        kwargs.setdefault('args', {})
        kwargs['args'].update(self.filtering_args)
        super().__init__(List(_type), *args, **kwargs)

    @staticmethod
    def list_resolver(manager, filterset_class, filtering_args,
                      root, args, context, info):
        filter_kwargs = {k: v for k, v in args.items() if k in filtering_args}
        qs = manager.get_queryset()
        qs = filterset_class(data=filter_kwargs, queryset=qs).qs
        return qs

    def get_resolver(self, parent_resolver):
        return partial(self.list_resolver, self.type._meta.model._default_manager,
                       self.filterset_class, self.filtering_args)
