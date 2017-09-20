import graphene
from django.utils import timezone
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from graphql_relay import from_global_id

from colegend.experience.models import add_experience
from colegend.scopes.models import Scope, get_scope_by_name
from colegend.scopes.schema import ScopeType
from colegend.journals.models import JournalEntry
from .models import InterviewEntry


class JournalEntryNode(DjangoObjectType):
    class Meta:
        model = JournalEntry
        filter_fields = {
            'scope': ['exact'],
            'start': ['exact', 'lt', 'gt', 'lte', 'gte'],
            'content': ['exact', 'icontains'],
            'keywords': ['exact', 'icontains'],
        }
        interfaces = [graphene.Node]


class JournalEntryQuery(graphene.ObjectType):
    journal_entry = graphene.Node.Field(JournalEntryNode)
    journal_entries = DjangoFilterConnectionField(JournalEntryNode)


class AddJournalEntryMutation(graphene.relay.ClientIDMutation):
    journal_entry = graphene.Field(JournalEntryNode)

    class Input:
        scope = ScopeType()
        start = graphene.types.datetime.DateTime()
        keywords = graphene.String()
        content = graphene.String()

    @classmethod
    def mutate_and_get_payload(cls, root, info, scope=Scope.DAY.value, start=None, content='', keywords=''):
        user = info.context.user
        if not start:
            start = get_scope_by_name(scope)().start
        entry = user.journal_entries.create(scope=scope, start=start, content=content, keywords=keywords)
        add_experience(user, 'studio', 1)
        return AddJournalEntryMutation(journal_entry=entry)


class UpdateJournalEntryMutation(graphene.relay.ClientIDMutation):
    success = graphene.Boolean()
    journal_entry = graphene.Field(JournalEntryNode)

    class Input:
        id = graphene.ID()
        keywords = graphene.String()
        content = graphene.String()

    @classmethod
    def mutate_and_get_payload(cls, root, info, id, keywords=None, content=None):
        user = info.context.user
        _type, id = from_global_id(id)
        entry = user.journal_entries.get(id=id)
        if keywords:
            entry.keywords = keywords
        if content:
            entry.content = content
        entry.save()
        return UpdateJournalEntryMutation(success=True, journal_entry=entry)


class JournalEntryMutation(graphene.ObjectType):
    add_journal_entry = AddJournalEntryMutation.Field()
    update_journal_entry = UpdateJournalEntryMutation.Field()


class InterviewEntryNode(DjangoObjectType):
    class Meta:
        model = InterviewEntry
        filter_fields = {
            'scope': ['exact'],
            'start': ['exact', 'lt', 'gt', 'lte', 'gte'],
        }
        interfaces = [graphene.Node]


class InterviewEntryQuery(graphene.ObjectType):
    interview_entry = graphene.Node.Field(InterviewEntryNode)
    interview_entries = DjangoFilterConnectionField(InterviewEntryNode)


class AddInterviewEntry(graphene.relay.ClientIDMutation):
    interview_entry = graphene.Field(InterviewEntryNode)

    class Input:
        scope = ScopeType()
        start = graphene.types.datetime.DateTime()
        likes = graphene.String()
        dislikes = graphene.String()

    @classmethod
    def mutate_and_get_payload(cls, root, info, scope=Scope.DAY.value, start=None, likes='', dislikes=''):
        user = info.context.user
        if not start:
            start = timezone.localdate(timezone.now())
        entry = user.interview_entries.create(scope=scope, start=start, likes=likes, dislikes=dislikes)
        return AddInterviewEntry(interview_entry=entry)


class UpdateInterviewEntry(graphene.relay.ClientIDMutation):
    success = graphene.Boolean()
    interview_entry = graphene.Field(InterviewEntryNode)

    class Input:
        id = graphene.ID()
        likes = graphene.String()
        dislikes = graphene.String()

    @classmethod
    def mutate_and_get_payload(cls, root, info, id, likes=None, dislikes=None):
        user = info.context.user
        _type, id = from_global_id(id)
        entry = user.interview_entries.get(id=id)
        if likes:
            entry.likes = likes
        if dislikes:
            entry.dislikes = dislikes
        entry.save()
        return UpdateInterviewEntry(success=True, interview_entry=entry)


class InterviewEntryMutation(graphene.ObjectType):
    add_interview_entry = AddInterviewEntry.Field()
    update_interview_entry = UpdateInterviewEntry.Field()


class StudioQuery(
    InterviewEntryQuery,
    JournalEntryQuery,
    graphene.ObjectType):
    pass


class StudioMutation(
    InterviewEntryMutation,
    JournalEntryMutation,
    graphene.ObjectType):
    pass
