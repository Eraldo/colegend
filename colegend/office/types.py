import graphene

from .models import Status

StatusType = graphene.Enum.from_enum(Status)
