import graphene
from .models import Scope

ScopeType = graphene.Enum.from_enum(Scope)
