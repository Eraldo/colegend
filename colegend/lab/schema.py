import graphene


class Upload(graphene.Scalar):
    def serialize(self):
        pass


# class UploadFiles(graphene.relay.ClientIDMutation):
#     success = graphene.Boolean()
#
#     class Input:
#         files = Upload()
#
#     @staticmethod
#     def mutate_and_get_payload(cls, info, files=None):
#         # # TODO: Remove breakpoint
#         # import ipdb; ipdb.set_trace()
#         print(cls, files)
#         files = info.context.FILES
#         print(files)
#         # files = context.files
#         # client_signature = files['variables.signature']
#         return UploadFiles(success=True)


class LabMutations(graphene.ObjectType):
    pass
    # upload = UploadFiles.Field()
