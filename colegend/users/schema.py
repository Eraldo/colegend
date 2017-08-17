import graphene
from graphene_django import DjangoObjectType

from .models import User
from graphene_django.converter import convert_django_field
from phonenumber_field.modelfields import PhoneNumberField


@convert_django_field.register(PhoneNumberField)
def convert_phone_number_to_string(field, registry=None):
    return graphene.String(description=field.help_text, required=not field.null)


class UserType(DjangoObjectType):
    class Meta:
        model = User


class Query(graphene.AbstractType):
    user = graphene.Field(
        UserType,
        id=graphene.Int(),
        name=graphene.String(),
    )
    all_users = graphene.List(UserType)

    def resolve_all_users(self, args, context, info):
        return User.objects.all()

    def resolve_user(self, args, context, info):
        id = args.get('id')
        name = args.get('name')

        if id is not None:
            return User.objects.get(id=id)

        if name is not None:
            return User.objects.get(name=name)

        return None
