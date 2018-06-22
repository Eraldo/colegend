import graphene


class Upload(graphene.Scalar):
    def serialize(self):
        pass


class UploadFiles(graphene.relay.ClientIDMutation):
    success = graphene.Boolean()

    class Input:
        files = Upload()

    @staticmethod
    def mutate_and_get_payload(cls, info, files=None):
        files = info.context.FILES
        # files = context.files
        # client_signature = files['variables.signature']
        return UploadFiles(success=True)


class LabMutations(graphene.ObjectType):
    # pass
    upload = UploadFiles.Field()
