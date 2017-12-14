import graphene
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from graphql_relay import from_global_id

from colegend.academy.forms import BookReviewForm
from colegend.experience.models import add_experience
from .models import Book, BookReview, BookTag
from .filters import BookFilter, BookReviewFilter


class BookTagNode(DjangoObjectType):

    class Meta:
        model = BookTag
        interfaces = [graphene.Node]
        filter_fields = {
            'name': ['exact', 'istartswith', 'icontains'],
        }


class BookTagQuery(graphene.ObjectType):
    book_tag = graphene.Node.Field(BookTagNode)
    book_tags = DjangoFilterConnectionField(BookTagNode)


class BookNode(DjangoObjectType):
    rating = graphene.Field(
        graphene.Float
    )
    area_ratings = graphene.Field(
        graphene.List(graphene.Float)
    )
    reviewed = graphene.Field(
        graphene.Boolean
    )

    class Meta:
        model = Book
        interfaces = [graphene.Node]

    def resolve_rating(self, info):
        return self.rating

    def resolve_area_ratings(self, info):
        return self.area_ratings.values()

    def resolve_reviewed(self, info):
        user = info.context.user
        return user.book_reviews.filter(book=self.id).exists()


class BookQuery(graphene.ObjectType):
    book = graphene.Node.Field(BookNode)
    books = DjangoFilterConnectionField(BookNode, filterset_class=BookFilter)
    featured_book = graphene.Field(BookNode)

    def resolve_featured_book(self, info):
        user = info.context.user
        book = Book.objects.filter(featured=True).first()
        return book


class BookReviewNode(DjangoObjectType):
    class Meta:
        model = BookReview
        interfaces = [graphene.Node]


class BookReviewQuery(graphene.ObjectType):
    book_review = graphene.Node.Field(BookReviewNode)
    book_reviews = DjangoFilterConnectionField(BookReviewNode, filterset_class=BookReviewFilter)


class CreateBookReviewMutation(graphene.relay.ClientIDMutation):
    review = graphene.Field(BookReviewNode)

    class Input:
        book = graphene.ID()
        rating = graphene.Int()
        area_1 = graphene.Int()
        area_2 = graphene.Int()
        area_3 = graphene.Int()
        area_4 = graphene.Int()
        area_5 = graphene.Int()
        area_6 = graphene.Int()
        area_7 = graphene.Int()
        content = graphene.String()

    @classmethod
    def mutate_and_get_payload(cls, root, info, book, rating, area_1, area_2, area_3, area_4, area_5, area_6, area_7, content):
        user = info.context.user
        _type, book = from_global_id(book)
        form = BookReviewForm({
            "owner": user.id,
            "book": book,
            "rating": rating,
            "area_1": area_1,
            "area_2": area_2,
            "area_3": area_3,
            "area_4": area_4,
            "area_5": area_5,
            "area_6": area_6,
            "area_7": area_7,
            "content": content,
        })
        if form.is_valid():
            review = form.save()
            add_experience(user, 'academy')
        else:
            raise Exception(form.errors.as_json())
        return CreateBookReviewMutation(review=review)


class BookReviewMutations(graphene.ObjectType):
    create_book_review = CreateBookReviewMutation.Field()


class AcademyQuery(
    BookTagQuery,
    BookQuery,
    BookReviewQuery,
    graphene.ObjectType):
    pass


class AcademyMutation(
    BookReviewMutations,
    graphene.ObjectType):
    pass
