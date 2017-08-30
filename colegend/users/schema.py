import graphene
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from .models import User
from graphene_django.converter import convert_django_field
from phonenumber_field.modelfields import PhoneNumberField


@convert_django_field.register(PhoneNumberField)
def convert_phone_number_to_string(field, registry=None):
    return graphene.String(description=field.help_text, required=not field.null)


class UserType(DjangoObjectType):
    class Meta:
        model = User
        filter_fields = {
            'name': ['exact', 'icontains', 'istartswith'],
        }
        interfaces = [graphene.Node]


class Query(graphene.ObjectType):
    user = graphene.Node.Field(UserType)
    users = DjangoFilterConnectionField(UserType)
    # user = graphene.Field(
    #     UserType,
    #     id=graphene.Int(),
    #     name=graphene.String(),
    # )
    # users = graphene.List(UserType)
    #
    # def resolve_users(self, info):
    #     return User.objects.all()
    #
    # def resolve_user(self, info, id=None, name=None):
    #     if id is not None:
    #         return User.objects.get(id=id)
    #     if name is not None:
    #         return User.objects.get(name=name)
    #     return None
