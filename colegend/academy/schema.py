import graphene
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

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

    class Meta:
        model = Book
        interfaces = [graphene.Node]

    def resolve_rating(self, info):
        return self.rating


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


class AcademyQuery(
    BookTagQuery,
    BookQuery,
    BookReviewQuery,
    graphene.ObjectType):
    pass


class AcademyMutation(
    graphene.ObjectType):
    pass
