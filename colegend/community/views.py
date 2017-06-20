from rest_framework import viewsets
from rest_framework.decorators import list_route
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .serializers import DuoSerializer, ClanSerializer, TribeSerializer
from .models import Duo, Tribe, Clan


class DuoViewSet(viewsets.ModelViewSet):
    queryset = Duo.objects.all()
    serializer_class = DuoSerializer

    @list_route(permission_classes=[IsAuthenticated])
    def owned(self, request):
        user = request.user
        serializer = self.get_serializer(user.duo)
        return Response(serializer.data)


class ClanViewSet(viewsets.ModelViewSet):
    queryset = Clan.objects.all()
    serializer_class = ClanSerializer


class TribeViewSet(viewsets.ModelViewSet):
    queryset = Tribe.objects.all()
    serializer_class = TribeSerializer
