import graphene

from colegend.api.utils import extract_file


class Upload(graphene.Scalar):
    def serialize(self):
        pass


class UploadFiles(graphene.relay.ClientIDMutation):
    success = graphene.Boolean()

    class Input:
        file = Upload()
        file2 = Upload()

    @staticmethod
    def mutate_and_get_payload(cls, info, **kwargs):
        file = extract_file(info)
        return UploadFiles(success=True)


class LabMutations(graphene.ObjectType):
    upload = UploadFiles.Field()
