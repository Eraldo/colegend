import graphene
import colegend.users.schema
import colegend.office.schema
import colegend.outcomes.schema


class Query(
    colegend.users.schema.Query,
    colegend.office.schema.Query,
    colegend.outcomes.schema.Query,
    graphene.ObjectType):
    # This class will inherit from multiple Queries
    # as we begin to add more apps to our project
    pass


schema = graphene.Schema(query=Query)
