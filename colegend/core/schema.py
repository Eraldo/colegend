from enum import Enum

import graphene


class MessageKind(Enum):
    DANGER = 'DANGER'
    WARNING = 'WARNING'
    INFO = 'INFO'
    SUCCESS = 'SUCCESS'


MessageKindType = graphene.Enum.from_enum(MessageKind)


class MessageNode(graphene.ObjectType):
    """
    A message model intended to be used to send information/feedback back to the frontend user.    """
    type = graphene.Field(MessageKindType)
    content = graphene.String()
