from enum import Enum

import graphene
from django.contrib.auth import authenticate
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from .models import User
from .filters import UserFilter
from graphene_django.converter import convert_django_field
from phonenumber_field.modelfields import PhoneNumberField


class App(Enum):
    HOME = 'home'
    ARCADE = 'arcade'
    OFFICE = 'office'
    COMMUNITY = 'community'
    STUDIO = 'studio'
    ACADEMY = 'academy'
    JOURNEY = 'journey'

AppType = graphene.Enum.from_enum(App)


@convert_django_field.register(PhoneNumberField)
def convert_phone_number_to_string(field, registry=None):
    return graphene.String(description=field.help_text, required=not field.null)


class UserNode(DjangoObjectType):
    level = graphene.Field(
        graphene.Int,
        app=AppType(),
    )
    experience = graphene.Field(
        graphene.Int,
        app=AppType(),
    )

    class Meta:
        model = User
        # filter_fields = {
        #     'name': ['exact', 'icontains', 'istartswith'],
        # }
        interfaces = [graphene.Node]

    def resolve_level(self, info, app=None):
        user = info.context.user
        kwargs = {}
        if app is not None:
            kwargs['app'] = app
        if user.is_authenticated:
            return user.experience.level(**kwargs)
        return 0

    def resolve_experience(self, info, app=None):
        user = info.context.user
        kwargs = {}
        if app is not None:
            kwargs['app'] = app
        if user.is_authenticated:
            return user.experience.total(**kwargs)
        return 0


class UserQuery(graphene.ObjectType):
    my_user = graphene.Field(
        UserNode
    )
    user = graphene.Node.Field(UserNode)
    users = DjangoFilterConnectionField(UserNode, filterset_class=UserFilter)

    def resolve_my_user(self, info):
        return info.context.user

    # def resolve_my_posts(self, args, context, info):
    #     # context will reference to the Django request
    #     if not context.user.is_authenticated():
    #         return Post.objects.none()
    #     else:
    #         return Post.objects.filter(owner=context.user)

    # user = graphene.Field(
    #     UserType,
    #     id=graphene.Int(),
    #     name=graphene.String(),
    # )

    # users = graphene.List(UserType)

    # def resolve_users(self, info):
    #     return User.objects.all()

    # def resolve_user(self, info, id=None, name=None):
    #     if id is not None:
    #         return User.objects.get(id=id)
    #     if name is not None:
    #         return User.objects.get(name=name)
    #     return None


class Login(graphene.relay.ClientIDMutation):
    user = graphene.Field(UserNode)
    token = graphene.String()

    class Input:
        email = graphene.String()
        password = graphene.String()

    @classmethod
    def mutate_and_get_payload(cls, root, info, email, password):
        user = authenticate(
            email=email,
            password=password,
        )
        return Login(user=user, token=user.auth_token)


class Logout(graphene.relay.ClientIDMutation):
    success = graphene.Boolean()

    @classmethod
    def mutate_and_get_payload(cls, root, info):
        user = info.context.user
        # TODO: Log user out.
        print(user.auth_token)
        # logout(request={"user": user})
        return Logout(success=False)


class UserMutation(graphene.ObjectType):
    login = Login.Field()
    logout = Logout.Field()
