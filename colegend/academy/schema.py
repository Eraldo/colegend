import graphene
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from .models import Book, BookReview


class BookNode(DjangoObjectType):
    class Meta:
        model = Book
        filter_fields = {
            'name': ['exact', 'istartswith', 'icontains'],
            'author': ['exact', 'istartswith', 'icontains'],
            'content': ['exact', 'icontains'],
            'featured': ['exact'],
        }
        interfaces = [graphene.Node]


class BookQuery(graphene.ObjectType):
    book = graphene.Node.Field(BookNode)
    books = DjangoFilterConnectionField(BookNode)
    featured_book = graphene.Field(BookNode)

    def resolve_featured_book(self, info):
        user = info.context.user
        book = Book.objects.filter(featured=True).first()
        return book


class BookReviewNode(DjangoObjectType):
    class Meta:
        model = BookReview
        filter_fields = {
            'book': ['exact'],
            'content': ['exact', 'icontains'],
            'area_1': ['exact', 'lt', 'gt', 'lte', 'gte'],
            'area_2': ['exact', 'lt', 'gt', 'lte', 'gte'],
            'area_3': ['exact', 'lt', 'gt', 'lte', 'gte'],
            'area_4': ['exact', 'lt', 'gt', 'lte', 'gte'],
            'area_5': ['exact', 'lt', 'gt', 'lte', 'gte'],
            'area_6': ['exact', 'lt', 'gt', 'lte', 'gte'],
            'area_7': ['exact', 'lt', 'gt', 'lte', 'gte'],
        }
        interfaces = [graphene.Node]


class BookReviewQuery(graphene.ObjectType):
    book_review = graphene.Node.Field(BookReviewNode)
    book_reviews = DjangoFilterConnectionField(BookReviewNode)
    featured_book_review = graphene.Field(BookReviewNode)

    def resolve_featured_book_review(self, info):
        user = info.context.user
        book_review = BookReview.objects.filter(featured=True).first()
        return book_review


class AcademyQuery(
    BookQuery,
    BookReviewQuery,
    graphene.ObjectType):
    pass


class AcademyMutation(
    graphene.ObjectType):
    pass
