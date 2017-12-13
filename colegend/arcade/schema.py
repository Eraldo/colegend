import graphene
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from colegend.api.models import DjangoUserFilterConnectionField
from .models import Adventure, AdventureReview, AdventureTag
from .filters import AdventureFilter, AdventureReviewFilter


class AdventureTagNode(DjangoObjectType):

    class Meta:
        model = AdventureTag
        interfaces = [graphene.Node]
        filter_fields = {
            'name': ['exact', 'istartswith', 'icontains'],
        }


class AdventureTagQuery(graphene.ObjectType):
    adventure_tag = graphene.Node.Field(AdventureTagNode)
    adventure_tags = DjangoFilterConnectionField(AdventureTagNode)


class AdventureNode(DjangoObjectType):
    rating = graphene.Field(
        graphene.Float
    )
    completed = graphene.Field(
        graphene.Boolean
    )

    class Meta:
        model = Adventure
        interfaces = [graphene.Node]

    def resolve_rating(self, info):
        return self.rating

    def resolve_completed(self, info):
        user = info.context.user
        return user.adventure_reviews.filter(adventure=self.id).exists()


class AdventureQuery(graphene.ObjectType):
    adventure = graphene.Node.Field(AdventureNode)
    adventures = DjangoUserFilterConnectionField(AdventureNode, filterset_class=AdventureFilter)


class AdventureReviewNode(DjangoObjectType):
    class Meta:
        model = AdventureReview
        interfaces = [graphene.Node]


class AdventureReviewQuery(graphene.ObjectType):
    adventure_review = graphene.Node.Field(AdventureReviewNode)
    adventure_reviews = DjangoFilterConnectionField(AdventureReviewNode, filterset_class=AdventureReviewFilter)


class ArcadeQuery(
    AdventureTagQuery,
    AdventureQuery,
    AdventureReviewQuery,
    graphene.ObjectType):
    pass


class ArcadeMutation(
    graphene.ObjectType):
    pass
