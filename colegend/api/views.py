# import json
#
# import six
# from django.http import HttpResponseBadRequest
from rest_auth.registration.views import SocialLoginView
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from graphene_django.views import GraphQLView as GrapheneGraphQLView, HttpError


class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter


class FacebookLogin(SocialLoginView):
    adapter_class = FacebookOAuth2Adapter


class GraphQLView(GrapheneGraphQLView):
    """
    Custom version of GraphQLView to handle file uploads.
    """
    # @staticmethod
    # def get_graphql_params(request, data):
    #     print(request.GET, request.POST, data)
    #     # # TODO: Remove breakpoint
    #     # import ipdb; ipdb.set_trace()
    #     if isinstance(data, str):
    #         data = {}
    #     # if not request.GET:
    #     #     print('no request.GET')
    #     #     request.GET = request.POST
    #
    #     query = request.GET.get('query') or data.get('query')
    #     variables = request.GET.get('variables') or data.get('variables')
    #     id = request.GET.get('id') or data.get('id')
    #     operation_name = None
    #
    #     # try to get params from POST
    #     if not query:
    #         if request.POST.get("operations"):
    #             parsed_post = json.loads(request.POST.get("operations"))
    #
    #             if 'query' in parsed_post:
    #                 query = parsed_post['query']
    #
    #             if 'variables' in parsed_post:
    #                 variables = parsed_post['variables']
    #
    #             if 'operationName' in parsed_post:
    #                 operation_name = parsed_post['operationName']
    #
    #     if variables and isinstance(variables, six.text_type):
    #         try:
    #             variables = json.loads(variables)
    #         except Exception:
    #             raise HttpError(HttpResponseBadRequest(
    #                 'Variables are invalid JSON.'))
    #
    #     operation_name = operation_name or request.GET.get(
    #         'operationName') or data.get('operationName')
    #     if operation_name == "null":
    #         operation_name = None
    #     # print(query, variables, operation_name, id)
    #     return query, variables, operation_name, id
