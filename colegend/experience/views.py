from rest_framework import viewsets
from rest_framework.decorators import list_route
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .serializers import ExperienceSerializer
from .models import Experience


class ExperienceViewSet(viewsets.ModelViewSet):
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer
    filter_fields = ['app', 'level']

    def get_queryset(self):
        user = self.request.user
        return user.experience.all()

    @list_route(permission_classes=[IsAuthenticated])
    def total(self, request):
        user = request.user

        params = request.query_params
        app = params.get('app', None)
        level = params.get('level', None)

        # TODO: Implementing filtering.

        amount = user.experience.total()
        content = {'amount': amount}
        return Response(content)

    @list_route(permission_classes=[IsAuthenticated])
    def level(self, request):
        user = request.user

        params = request.query_params
        app = params.get('app', None)

        # TODO: Implementing filtering.

        level = user.experience.level()
        content = {'level': level}
        return Response(content)
