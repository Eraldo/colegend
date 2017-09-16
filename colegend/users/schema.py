from enum import Enum

import graphene
from django.contrib.auth import authenticate
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from graphql_relay import from_global_id

from .models import User
from .filters import UserFilter
from graphene_django.converter import convert_django_field
from phonenumber_field.modelfields import PhoneNumberField


class Size(Enum):
    SMALL = 'small'
    MEDIUM = 'medium'
    LARGE = 'large'


SizeType = graphene.Enum.from_enum(Size)


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
    avatar = graphene.Field(
        graphene.String,
        size=SizeType(),
    )

    class Meta:
        model = User
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

    def resolve_avatar(self, info, size=Size.MEDIUM.value):
        if not self.avatar:
            return ''
        url = self.avatar[size].url
        return info.context.build_absolute_uri(url)


class UserQuery(graphene.ObjectType):
    my_user = graphene.Field(UserNode)
    user = graphene.Node.Field(UserNode)
    users = DjangoFilterConnectionField(UserNode, filterset_class=UserFilter)

    def resolve_my_user(self, info):
        return info.context.user


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


class UpdateUser(graphene.relay.ClientIDMutation):
    user = graphene.Field(UserNode)

    class Input:
        name = graphene.String()
        username = graphene.String()
        gender = graphene.String()
        purpose = graphene.String()
        status = graphene.String()

    @classmethod
    def mutate_and_get_payload(cls, root, info, username=None, name=None, gender=None, purpose=None, status=None):
        user = info.context.user
        if username:
            user.username = username
        if name:
            user.name = name
        if gender:
            user.gender = gender
        if purpose:
            user.purpose = purpose
        if status:
            user.status = status
        user.save()
        return UpdateUser(user=user)


class ContactUser(graphene.relay.ClientIDMutation):
    success = graphene.Boolean()

    class Input:
        id = graphene.ID()
        subject = graphene.String()
        message = graphene.String()

    @classmethod
    def mutate_and_get_payload(cls, root, info, id=None, subject=None, message=None):
        # Sending email and returning True on success.
        user = info.context.user
        _type, id = from_global_id(id)
        receiver = User.objects.get(id=id)
        receiver.contact(user, subject, message)
        return ContactUser(success=True)


class UserMutation(graphene.ObjectType):
    login = Login.Field()
    logout = Logout.Field()
    update_user = UpdateUser.Field()
    contact_user = ContactUser.Field()
