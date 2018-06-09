import graphene
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from graphql_relay import from_global_id

from colegend.api.models import DjangoUserFilterConnectionField, CountableConnectionBase
from colegend.experience.models import add_experience
from .models import Adventure, AdventureReview, AdventureTag, Deck, Card
from .filters import AdventureFilter, AdventureReviewFilter
from .forms import AdventureReviewForm


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
        user = info.context.user
        try:
            review = user.adventure_reviews.get(adventure=self.id)
            return review.rating
        except AdventureReview.DoesNotExist:
            return

    def resolve_completed(self, info):
        user = info.context.user
        return user.adventure_reviews.filter(adventure=self.id).exists()

    def resolve_image(self, info):
        if self.image:
            return info.context.build_absolute_uri(self.image.url)
        return ''


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


class CreateAdventureReviewMutation(graphene.relay.ClientIDMutation):
    review = graphene.Field(AdventureReviewNode)

    class Input:
        adventure = graphene.ID()
        rating = graphene.Int()
        content = graphene.String()
        image_url = graphene.String()

    @classmethod
    def mutate_and_get_payload(cls, root, info, adventure, rating, content, **kwargs):
        user = info.context.user
        _type, adventure = from_global_id(adventure)
        form = AdventureReviewForm({
            "owner": user.id,
            "adventure": adventure,
            "rating": rating,
            "content": content,
            **kwargs
        })
        if form.is_valid():
            review = form.save()
            add_experience(user, 'arcade')
        else:
            raise Exception(form.errors.as_json())
        return CreateAdventureReviewMutation(review=review)


class AdventureReviewMutations(graphene.ObjectType):
    create_adventure_review = CreateAdventureReviewMutation.Field()


class DeckNode(DjangoObjectType):
    class Meta:
        model = Deck
        filter_fields = {
            'name': ['exact', 'istartswith', 'icontains'],
            'content': ['exact', 'icontains'],
        }
        connection_class = CountableConnectionBase
        interfaces = [graphene.Node]

    def resolve_image(self, info):
        if not self.image:
            return ''
        url = self.image.url
        return info.context.build_absolute_uri(url)


class DeckQuery(graphene.ObjectType):
    deck = graphene.Node.Field(DeckNode)
    decks = DjangoFilterConnectionField(DeckNode)


class CardNode(DjangoObjectType):
    class Meta:
        model = Card
        filter_fields = {
            'name': ['exact', 'istartswith', 'icontains'],
            'content': ['exact', 'icontains'],
        }
        connection_class = CountableConnectionBase
        interfaces = [graphene.Node]

    def resolve_image(self, info):
        if not self.image:
            return ''
        url = self.image.url
        return info.context.build_absolute_uri(url)


class CardQuery(graphene.ObjectType):
    card = graphene.Node.Field(CardNode)
    cards = DjangoFilterConnectionField(CardNode)


class ArcadeQuery(
    AdventureTagQuery,
    AdventureQuery,
    AdventureReviewQuery,
    DeckQuery,
    CardQuery,
    graphene.ObjectType):
    pass


class ArcadeMutation(
    AdventureReviewMutations,
    graphene.ObjectType):
    pass
