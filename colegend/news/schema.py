import graphene
from django.utils import timezone
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from .models import News


class NewsNode(DjangoObjectType):
    class Meta:
        model = News
        filter_fields = {
            'name': ['exact', 'istartswith', 'icontains'],
            'author': ['exact'],
            'author__name': ['icontains'],
            'date': ['exact', 'lt', 'gt', 'lte', 'gte'],
            'content': ['exact', 'icontains'],
            'description': ['exact', 'icontains'],

        }
        interfaces = [graphene.Node]


class NewsQuery(graphene.ObjectType):
    news_item = graphene.Node.Field(NewsNode)
    news_items = DjangoFilterConnectionField(NewsNode)
    latest_news = graphene.Field(NewsNode)

    def resolve_latest_news(self, info):
        user = info.context.user
        news = News.objects.first()
        return news


class AddNews(graphene.relay.ClientIDMutation):
    news = graphene.Field(NewsNode)

    class Input:
        name = graphene.String()
        author = graphene.ID()
        date = graphene.types.datetime.DateTime()
        image_url = graphene.String()
        description = graphene.String()
        content = graphene.String()

    @classmethod
    def mutate_and_get_payload(cls, root, info, *args, **kwargs):
        user = info.context.user
        if not kwargs.get('author'):
            kwargs['author'] = user
        news = News.objects.create(*args, **kwargs)
        return AddNews(news=news)


class NewsMutation(graphene.ObjectType):
    add_news = AddNews.Field()
