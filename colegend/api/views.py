from django.contrib.auth.models import Group
from rest_framework import viewsets

from rest_auth.registration.views import SocialLoginView
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter

from colegend.users.models import User
from colegend.users.serializers import UserSerializer, GroupSerializer
from colegend.outcomes.models import Outcome
from colegend.outcomes.serializers import OutcomeSerializer
from colegend.office.models import Focus
from colegend.office.serializers import FocusSerializer


class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter


class FacebookLogin(SocialLoginView):
    adapter_class = FacebookOAuth2Adapter


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class OutcomeViewSet(viewsets.ModelViewSet):
    queryset = Outcome.objects.all()
    serializer_class = OutcomeSerializer

    def get_queryset(self):
        user = self.request.user
        return user.outcomes.all()


class FocusViewSet(viewsets.ModelViewSet):
    queryset = Focus.objects.all()
    serializer_class = FocusSerializer

    def get_queryset(self):
        user = self.request.user
        return user.focuses.all()
