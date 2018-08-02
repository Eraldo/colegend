import graphene
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from graphql_relay import from_global_id

from colegend.api.models import CountableConnectionBase
from colegend.experience.models import add_experience
from .models import Hero, Demon, Quote, Quest, QuestObjective, UserQuestStatus, Tension


class QuestNode(DjangoObjectType):
    class Meta:
        model = Quest
        interfaces = [graphene.Node]


class QuestObjectiveNode(DjangoObjectType):
    class Meta:
        model = QuestObjective
        interfaces = [graphene.Node]


class UserQuestStatusNode(DjangoObjectType):
    previous = graphene.Field(lambda: UserQuestStatusNode)
    next = graphene.Field(lambda: UserQuestStatusNode)

    class Meta:
        model = UserQuestStatus
        interfaces = [graphene.Node]
        connection_class = CountableConnectionBase

    def resolve_next(self, info):
        return self.get_next()

    def resolve_previous(self, info):
        return self.get_previous()


class UserQuestStatusQuery(graphene.ObjectType):
    # user_quest_status = graphene.Node.Field(UserQuestStatusNode)
    # user_quest_statuses = DjangoFilterConnectionField(UserQuestStatusNode)
    current_quest_status = graphene.Field(UserQuestStatusNode, id=graphene.ID())

    def resolve_current_quest_status(self, info, id=None):
        user = info.context.user
        # Getting the status of the current or next quest.
        if id is not None:
            _type, id = from_global_id(id)
            current_quest = user.quest_statuses.get(id=id)
        else:
            current_quest = user.quest_statuses.last()
        if not current_quest:
            first_quest = Quest.objects.first()
            if first_quest:
                current_quest = user.quest_statuses.create(
                    quest=first_quest,
                )
        return current_quest


class AcceptGuidelinesMutation(graphene.relay.ClientIDMutation):
    success = graphene.Boolean()

    class Input:
        pass

    @classmethod
    def mutate_and_get_payload(cls, root, info):
        user = info.context.user
        if user.is_authenticated:
            checkpoint = user.add_checkpoint('guidelines accepted')
            quest_status = user.quest_statuses.first()
            if checkpoint and quest_status:
                objective = QuestObjective.objects.get(code='guidelines_accept')
                quest_status.complete_objective(objective)
        return AcceptGuidelinesMutation(success=True)


class EnableChatMutation(graphene.relay.ClientIDMutation):
    success = graphene.Boolean()

    class Input:
        pass

    @classmethod
    def mutate_and_get_payload(cls, root, info):
        user = info.context.user
        success = False
        if user.is_authenticated:
            checkpoint = user.add_checkpoint('chat')
            quest_status = user.quest_statuses.first()
            if checkpoint and quest_status and not quest_status.is_complete:
                objective = QuestObjective.objects.get(code='chat_join')
                quest_status.complete_objective(objective)
                success = True
                add_experience(user, 'journey')
        return AcceptGuidelinesMutation(success=success)


class QuestMutation(graphene.ObjectType):
    enable_chat = EnableChatMutation.Field()
    accept_guidelines = AcceptGuidelinesMutation.Field()


class HeroNode(DjangoObjectType):
    class Meta:
        model = Hero
        filter_fields = {
            'content': ['icontains'],
        }
        interfaces = [graphene.Node]


class HeroQuery(graphene.ObjectType):
    hero = graphene.Node.Field(HeroNode)
    heroes = DjangoFilterConnectionField(HeroNode)


class UpdateHeroMutation(graphene.relay.ClientIDMutation):
    success = graphene.Boolean()
    hero = graphene.Field(HeroNode)

    class Input:
        name = graphene.String()
        avatar = graphene.String()
        year_topic = graphene.String()
        vision = graphene.String()
        mission = graphene.String()
        values = graphene.String()
        powers = graphene.String()
        skills = graphene.String()
        habits = graphene.String()
        principles = graphene.String()
        wishes = graphene.String()
        goals = graphene.String()
        people = graphene.String()
        resources = graphene.String()
        achievements = graphene.String()
        questions = graphene.String()
        experiments = graphene.String()
        projects = graphene.String()
        bucket = graphene.String()
        roles = graphene.String()
        strategy = graphene.String()
        topics = graphene.String()
        inspirations = graphene.String()
        routines = graphene.String()
        blueprint_day = graphene.String()
        blueprint_week = graphene.String()
        blueprint_month = graphene.String()
        content = graphene.String()

    @classmethod
    def mutate_and_get_payload(cls, root, info, **kwargs):
        user = info.context.user
        hero = user.hero
        for key, value in kwargs.items():
            if value is not None:
                setattr(hero, key, value)
        hero.save()
        return UpdateHeroMutation(success=True, hero=hero)


class HeroMutation(graphene.ObjectType):
    update_hero = UpdateHeroMutation.Field()


class DemonNode(DjangoObjectType):
    class Meta:
        model = Demon
        filter_fields = {
            'content': ['icontains'],
        }
        interfaces = [graphene.Node]


class DemonQuery(graphene.ObjectType):
    demon = graphene.Node.Field(DemonNode)
    demons = DjangoFilterConnectionField(DemonNode)


class UpdateDemonMutation(graphene.relay.ClientIDMutation):
    success = graphene.Boolean()
    demon = graphene.Field(DemonNode)

    class Input:
        name = graphene.String()
        avatar = graphene.String()
        tensions = graphene.String()
        fears = graphene.String()
        content = graphene.String()

    @classmethod
    def mutate_and_get_payload(cls, root, info, **kwargs):
        user = info.context.user
        demon = user.demon
        for key, value in kwargs.items():
            if value is not None:
                setattr(demon, key, value)
        demon.save()
        return UpdateDemonMutation(success=True, demon=demon)


class TensionNode(DjangoObjectType):
    class Meta:
        model = Tension
        filter_fields = {
            'name': ['icontains'],
            'content': ['icontains'],
        }
        interfaces = [graphene.Node]
        connection_class = CountableConnectionBase


class TensionQuery(graphene.ObjectType):
    tension = graphene.Node.Field(TensionNode)
    tensions = DjangoFilterConnectionField(TensionNode)


class CreateTensionMutation(graphene.relay.ClientIDMutation):
    tension = graphene.Field(TensionNode)

    class Input:
        name = graphene.String()
        content = graphene.String()

    @classmethod
    def mutate_and_get_payload(cls, root, info, *args, **kwargs):
        user = info.context.user
        print(args, kwargs)
        tension = user.tensions.create(*args, **kwargs)
        return CreateTensionMutation(tension=tension)


class UpdateTensionMutation(graphene.relay.ClientIDMutation):
    tension = graphene.Field(TensionNode)

    class Input:
        name = graphene.String()
        content = graphene.String()

    @classmethod
    def mutate_and_get_payload(cls, root, info, id, **kwargs):
        user = info.context.user
        _type, id = from_global_id(id)
        tension = user.tensions.get(id=id)

        for key, value in kwargs.items():
            if value is not None:
                setattr(tension, key, value)
        tension.save()
        return UpdateDemonMutation(tension=tension)


class DeleteTensionMutation(graphene.relay.ClientIDMutation):
    success = graphene.Boolean()

    class Input:
        id = graphene.ID()

    @classmethod
    def mutate_and_get_payload(cls, root, info, id):
        user = info.context.user
        _type, id = from_global_id(id)
        tension = user.tensions.get(id=id)
        tension.delete()
        return DeleteTensionMutation(success=True)


class TensionMutation(graphene.ObjectType):
    create_tension = CreateTensionMutation.Field()
    update_tension = UpdateTensionMutation.Field()
    delete_tension = DeleteTensionMutation.Field()


class AddTensionMutation(graphene.relay.ClientIDMutation):
    demon = graphene.Field(DemonNode)

    class Input:
        tension = graphene.String()

    @classmethod
    def mutate_and_get_payload(cls, root, info, tension=''):
        user = info.context.user
        demon = user.demon
        if tension:
            demon.tensions += '{prefix}+ {tension}'.format(
                prefix='\n' if demon.tensions else '',
                tension=tension
            )
        demon.save()
        return AddTensionMutation(demon=demon)


class DemonMutation(graphene.ObjectType):
    update_demon = UpdateDemonMutation.Field()
    add_tension = AddTensionMutation.Field()


class QuoteNode(DjangoObjectType):
    liked = graphene.Field(
        graphene.Boolean
    )
    disliked = graphene.Field(
        graphene.Boolean
    )

    class Meta:
        model = Quote
        filter_fields = {
            'name': ['exact', 'icontains', 'istartswith'],
            'content': ['exact', 'icontains', 'istartswith'],
            'author': ['exact', 'icontains', 'istartswith'],
            'categories': ['exact'],
            'accepted': ['exact'],
            'used_as_daily': ['exact', 'lt', 'gt', 'lte', 'gte'],
        }
        interfaces = [graphene.Node]

    def resolve_liked(self, info):
        user = info.context.user
        return user.liked_quotes.filter(id=self.id).exists()

    def resolve_disliked(self, info):
        user = info.context.user
        return user.disliked_quotes.filter(id=self.id).exists()


class QuoteQuery(graphene.ObjectType):
    quote = graphene.Node.Field(QuoteNode)
    quotes = DjangoFilterConnectionField(QuoteNode)
    daily_quote = graphene.Field(QuoteNode)

    def resolve_daily_quote(self, info):
        return Quote.objects.daily_quote()
#
#
# class FeedbackQuoteMutation(graphene.relay.ClientIDMutation):
#     success = graphene.Boolean()
#     quote = graphene.Field(QuoteNode)
#
#     class Input:
#         id = graphene.ID()
#         liked = graphene.Boolean()
#         disliked = graphene.Boolean()
#
#     @classmethod
#     def mutate_and_get_payload(cls, root, info, id, liked=None, disliked=None):
#         user = info.context.user
#         _type, id = from_global_id(id)
#         quote = Quote.objects.get(id=id)
#
#         # Make sure either liked or disliked was selected.
#         if liked is None and disliked is None:
#             raise Exception('Please provide feedback.')
#         if liked is not None and disliked is not None:
#             raise Exception('Please either like or dislike.')
#
#         if liked is not None:
#             quote.like(user)
#         elif disliked is not None:
#             quote.dislike(user)
#
#         return FeedbackQuoteMutation(success=True, quote=quote)


class LikeQuoteMutation(graphene.relay.ClientIDMutation):
    success = graphene.Boolean()
    quote = graphene.Field(QuoteNode)

    class Input:
        id = graphene.ID()

    @classmethod
    def mutate_and_get_payload(cls, root, info, id):
        user = info.context.user
        _type, id = from_global_id(id)
        quote = Quote.objects.get(id=id)
        quote.like(user)
        return LikeQuoteMutation(success=True, quote=quote)


class DislikeQuoteMutation(graphene.relay.ClientIDMutation):
    success = graphene.Boolean()
    quote = graphene.Field(QuoteNode)

    class Input:
        id = graphene.ID()

    @classmethod
    def mutate_and_get_payload(cls, root, info, id):
        user = info.context.user
        _type, id = from_global_id(id)
        quote = Quote.objects.get(id=id)
        quote.dislike(user)
        return DislikeQuoteMutation(success=True, quote=quote)


class QuoteMutation(graphene.ObjectType):
    like_quote = LikeQuoteMutation.Field()
    dislike_quote = DislikeQuoteMutation.Field()


class JourneyQuery(
    HeroQuery,
    DemonQuery,
    TensionQuery,
    QuoteQuery,
    UserQuestStatusQuery,
    graphene.ObjectType):
    pass


class JourneyMutation(
    HeroMutation,
    DemonMutation,
    TensionMutation,
    QuoteMutation,
    QuestMutation,
    graphene.ObjectType):
    pass
