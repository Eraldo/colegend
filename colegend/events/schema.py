import graphene
from django.utils import timezone
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from .models import Event


class EventNode(DjangoObjectType):
    class Meta:
        model = Event
        filter_fields = {
            'name': ['exact', 'istartswith', 'icontains'],
            'start': ['exact', 'lt', 'gt', 'lte', 'gte'],
            'end': ['exact', 'lt', 'gt', 'lte', 'gte'],
            'content': ['exact', 'icontains'],
            'description': ['exact', 'icontains'],

        }
        interfaces = [graphene.Node]


class EventQuery(graphene.ObjectType):
    event = graphene.Node.Field(EventNode)
    events = DjangoFilterConnectionField(EventNode)
    next_event = graphene.Field(EventNode)

    def resolve_next_event(self, info):
        user = info.context.user
        today = timezone.localtime(timezone.now()).date()
        event = Event.objects.filter(start__gte=today).first()
        return event


class CreateEventMutation(graphene.relay.ClientIDMutation):
    event = graphene.Field(EventNode)

    class Input:
        name = graphene.String()
        start = graphene.types.datetime.DateTime()
        end = graphene.types.datetime.DateTime()
        location = graphene.String()
        image_url = graphene.String()
        video_url = graphene.String()
        description = graphene.String()
        content = graphene.String()

    @classmethod
    def mutate_and_get_payload(cls, root, info, *args, **kwargs):
        user = info.context.user
        event = Event.objects.create(*args, **kwargs)
        return CreateEventMutation(event=event)


class EventMutation(graphene.ObjectType):
    create_event = CreateEventMutation.Field()
