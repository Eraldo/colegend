import graphene
import colegend.users.schema
import colegend.office.schema
import colegend.outcomes.schema


class Query(
    colegend.users.schema.UserQuery,
    colegend.office.schema.FocusQuery,
    colegend.outcomes.schema.OutcomeQuery,
    graphene.ObjectType):
    # This class will inherit from multiple Queries
    # as we begin to add more apps to our project
    pass


class Mutation(
    colegend.users.schema.UserMutation,
    graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
