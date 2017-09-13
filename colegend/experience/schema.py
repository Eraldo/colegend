# import graphene
# from graphene_django import DjangoObjectType
#
# from colegend.users.schema import UserType
# from .models import Experience
#
#
# class ExperienceType(graphene.ObjectType):
#     level = graphene.Int()
#     experience = graphene.Int()
#     area_1 = graphene.Int()
#     area_2 = graphene.Int()
#     area_3 = graphene.Int()
#     area_4 = graphene.Int()
#     area_5 = graphene.Int()
#     area_6 = graphene.Int()
#     area_7 = graphene.Int()
#
#
# class Query(graphene.ObjectType):
#     experience = graphene.Field(
#         ExperienceType,
#         app=graphene.String(),
#     )
#
#     def resolve_experience(self, info):
#         return Experience.objects.all()
#
#     def resolve_outcome(self, info, app=None, name=None):
#         user = info.user
#
#         if app is not None:
#             return Outcome.objects.get(id=id)
#         if name is not None:
#             return Outcome.objects.get(name=name)
#         return None
#
