from django.contrib.auth.models import Group
from rest_framework import viewsets

from colegend.users.models import User
from colegend.users.serializers import UserSerializer, GroupSerializer
from colegend.outcomes.models import Outcome
from colegend.outcomes.serializers import OutcomeSerializer
from colegend.office.models import Focus
from colegend.office.serializers import FocusSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class OutcomeViewSet(viewsets.ModelViewSet):
    queryset = Outcome.objects.all()
    serializer_class = OutcomeSerializer


class FocusViewSet(viewsets.ModelViewSet):
    queryset = Focus.objects.all()
    serializer_class = FocusSerializer
