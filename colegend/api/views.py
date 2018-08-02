# import json
#
# import six
# from django.http import HttpResponseBadRequest
import json

from graphene_django.views import GraphQLView as GrapheneGraphQLView
from rest_auth.registration.views import SocialLoginView
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter


class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter


class FacebookLogin(SocialLoginView):
    adapter_class = FacebookOAuth2Adapter


class GraphQLView(GrapheneGraphQLView):
    """
    Custom version of GraphQLView to handle file uploads.
    """
    @staticmethod
    def get_graphql_params(request, data):
        """
        Workaround for createUploadLink
        :param request:
        :param data:
        :return:
        """
        if 'operations' in request.POST:
            data = json.loads(request.POST.get('operations'))
        return GrapheneGraphQLView.get_graphql_params(request, data)
