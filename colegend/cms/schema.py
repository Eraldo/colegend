import graphene
from graphene import Scalar
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from graphene_django.converter import convert_django_field
from wagtail.core.fields import StreamField

from colegend.api.models import CountableConnectionBase
from .models import ContentPage


class GenericStreamFieldType(Scalar):
    @staticmethod
    def serialize(stream_value):
        return stream_value.stream_data


@convert_django_field.register(StreamField)
def convert_stream_field(field, registry=None):
    return GenericStreamFieldType(
        description=field.help_text, required=not field.null
    )


class ContentPageNode(DjangoObjectType):
    class Meta:
        model = ContentPage
        filter_fields = {
            'title': ['exact', 'istartswith', 'icontains'],
            'owner': ['exact'],
            # 'content': ['exact', 'icontains'],
        }
        interfaces = [graphene.Node]
        connection_class = CountableConnectionBase


class PageQuery(graphene.ObjectType):
    content_page = graphene.Node.Field(ContentPageNode)
    content_pages = DjangoFilterConnectionField(ContentPageNode)


class PageMutation(graphene.ObjectType):
    pass
