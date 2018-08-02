from enum import Enum

import graphene
from allauth.account.signals import user_signed_up
from django.contrib.auth import authenticate, login, logout
from django.core.mail import EmailMessage
from django_slack import slack_message
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from graphql_relay import from_global_id
from rest_framework.authtoken.models import Token

from colegend.api.models import CountableConnectionBase
from colegend.api.utils import extract_file
from colegend.lab.schema import Upload
from colegend.office.filters import FocusFilter
from colegend.office.schema import FocusNode
from colegend.outcomes.filters import OutcomeFilter, StepFilter
from colegend.outcomes.schema import OutcomeNode, StepNode
from colegend.studio.filters import JournalEntryFilter
from colegend.studio.schema import JournalEntryNode
from .models import User
from .filters import UserFilter
from graphene_django.converter import convert_django_field
from phonenumber_field.modelfields import PhoneNumberField


class Size(Enum):
    MINI = 'MINI'
    SMALL = 'SMALL'
    MEDIUM = 'MEDIUM'
    LARGE = 'LARGE'


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
    notes = graphene.Field(
        graphene.String,
    )

    # Workaround: https://github.com/graphql-python/graphene-django/issues/273
    outcomes = DjangoFilterConnectionField(OutcomeNode, filterset_class=OutcomeFilter)
    steps = DjangoFilterConnectionField(StepNode, filterset_class=StepFilter)
    focuses = DjangoFilterConnectionField(FocusNode, filterset_class=FocusFilter)
    journal_entries = DjangoFilterConnectionField(JournalEntryNode, filterset_class=JournalEntryFilter)

    class Meta:
        model = User
        interfaces = [graphene.Node]
        connection_class = CountableConnectionBase

    def resolve_level(self, info, app=None):
        # print('>> level')
        user = info.context.user
        kwargs = {}
        if app is not None:
            kwargs['app'] = app
        if user.is_authenticated:
            return self.experience.level(**kwargs)
        return 0

    def resolve_experience(self, info, app=None):
        # print('>> experience')
        user = info.context.user
        kwargs = {}
        if app is not None:
            kwargs['app'] = app
        if user.is_authenticated:
            return self.experience.total(**kwargs)
        return 0

    def resolve_title(self, info):
        # print('>> title')
        return self.title or 'Tourist'

    def resolve_avatar(self, info, size=Size.MEDIUM.value):
        # print('>> avatar')
        if not self.avatar:
            return self.get_avatar_fallback()
        url = self.avatar[size].url
        return info.context.build_absolute_uri(url)

    def resolve_notes(self, info):
        # print('>> notes')
        user = info.context.user
        if not user.is_superuser:
            return ''
        return self.notes

    def resolve_mentor(self, info):
        # print('>> mentor')
        user = info.context.user
        if user.is_authenticated:
            # TODO: Fixing hardcoded mentor. => Get available mentor.
            return User.objects.get(username='Eraldo')
        return User.objects.none()


class UserQuery(graphene.ObjectType):
    users = DjangoFilterConnectionField(UserNode, filterset_class=UserFilter)
    user = graphene.Node.Field(UserNode)
    my_user = graphene.Field(UserNode)
    viewer = graphene.Field(UserNode)
    is_authenticated = graphene.Boolean()
    user_exists = graphene.Boolean(email=graphene.String())

    def resolve_my_user(self, info):
        # print('>> my user')
        user = info.context.user
        if user.is_authenticated:
            return user
        return None

    def resolve_viewer(self, info):
        # print('>> viewer')
        user = info.context.user
        if user.is_authenticated:
            return user
        return None

    def resolve_is_authenticated(self, info):
        # print('>> authenticated')
        return info.context.user.is_authenticated

    def resolve_user_exists(self, info, email):
        # print('>> user exists')
        return User.objects.filter(email=email).exists()


class JoinMutation(graphene.relay.ClientIDMutation):
    user = graphene.Field(UserNode)
    token = graphene.String()

    class Input:
        email = graphene.String()
        password = graphene.String()
        username = graphene.String()
        name = graphene.String()

    @classmethod
    def mutate_and_get_payload(cls, root, info, email, password, username, name='Someone'):
        # print('>> join')
        user = User.objects.create_user(username, email, password, name=name)
        Token.objects.get_or_create(user=user)
        user = authenticate(
            email=email,
            password=password,
        )
        user_signed_up.send(
            sender=user.__class__,
            request=info,
            user=user
        )
        return JoinMutation(user=user, token=user.auth_token)


class LoginMutation(graphene.relay.ClientIDMutation):
    user = graphene.Field(UserNode)
    token = graphene.String()

    class Input:
        email = graphene.String()
        password = graphene.String()

    @classmethod
    def mutate_and_get_payload(cls, root, info, email, password):
        # print('>> login')
        user = authenticate(
            email=email,
            password=password,
        )
        if user.is_active:
            login(info.context, user, user.backend)
        else:
            raise Exception('Account is disabled.')
        return LoginMutation(user=user, token=user.auth_token)


class LogoutMutation(graphene.relay.ClientIDMutation):
    success = graphene.Boolean()

    @classmethod
    def mutate_and_get_payload(cls, root, info):
        # print('>> logout')
        user = info.context.user
        logout(request=info.context)
        return LogoutMutation(success=True)


class UpdateUserMutation(graphene.relay.ClientIDMutation):
    user = graphene.Field(UserNode)

    class Input:
        name = graphene.String()
        username = graphene.String()
        avatar = Upload()
        gender = graphene.String()
        purpose = graphene.String()
        status = graphene.String()
        registration_country = graphene.String()

    @classmethod
    def mutate_and_get_payload(cls, root, info, username=None, name=None, avatar=None, gender=None, purpose=None, status=None,
                               registration_country=None):
        # print('>> update user')
        user = info.context.user
        if username:
            user.username = username
        if name:
            user.name = name
        avatar = extract_file(info)
        if avatar:
            user.avatar = avatar
        if gender:
            user.gender = gender
        if purpose:
            user.purpose = purpose
        if status:
            user.status = status
        if registration_country:
            user.registration_country = registration_country
        user.save()
        return UpdateUserMutation(user=user)


class ContactUserMutation(graphene.relay.ClientIDMutation):
    # Contacting another user.
    success = graphene.Boolean()

    class Input:
        id = graphene.ID()
        subject = graphene.String()
        message = graphene.String()

    @classmethod
    def mutate_and_get_payload(cls, root, info, id=None, subject=None, message=None):
        # print('>> contact user')
        user = info.context.user
        _type, id = from_global_id(id)
        receiver = User.objects.get(id=id)
        receiver.contact(user, subject, message)
        return ContactUserMutation(success=True)


class SendFeedbackMutation(graphene.relay.ClientIDMutation):
    # Sending feedback to the project.
    success = graphene.Boolean()
    user = graphene.Field(UserNode)

    class Input:
        subject = graphene.String()
        message = graphene.String()

    @classmethod
    def mutate_and_get_payload(cls, root, info, subject=None, message=None):
        user = info.context.user
        sender = user
        cls.send_feeback(user, subject, message)
        return SendFeedbackMutation(success=True, user=user)

    @staticmethod
    def send_feeback(sender, subject='', message=''):
        # TODO: Getting managers via dynamic role filtering.
        managers = ['connect@colegend.org']

        if subject:
            message = '{subject}\n{message}'.format(subject=subject, message=message)

        subject = 'Feedback from {name} ({username})'.format(name=sender.name, username=sender.username)

        email = EmailMessage(subject=subject, body=message, to=managers, reply_to=[sender.email])
        email.send()

        slack_message('slack/message.slack', {'message': '@channel: {}'.format(message), }, fail_silently=True)


class AddUserNoteMutation(graphene.relay.ClientIDMutation):
    user = graphene.Field(UserNode)

    class Input:
        id = graphene.ID()
        note = graphene.String()

    @classmethod
    def mutate_and_get_payload(cls, root, info, id, note=''):
        # print('>> add note to user')
        viewer = info.context.user
        if viewer.is_superuser:
            _type, id = from_global_id(id)
            user = User.objects.get(id=id)
            user.add_note(note)
        return UpdateUserMutation(user=user)


class UserMutation(graphene.ObjectType):
    join = JoinMutation.Field()
    login = LoginMutation.Field()
    logout = LogoutMutation.Field()
    update_user = UpdateUserMutation.Field()
    contact_user = ContactUserMutation.Field()
    send_feedback = SendFeedbackMutation.Field()
