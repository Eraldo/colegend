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

        # Filtering by app and level if given.
        kwargs = {}
        params = request.query_params
        app = params.get('app', None)
        level = params.get('level', None)
        if app:
            kwargs['app'] = app
        if level is not None:
            kwargs['level'] = level

        amount = user.experience.total(**kwargs)
        content = amount
        return Response(content)

    @list_route(permission_classes=[IsAuthenticated])
    def level(self, request):
        user = request.user

        # Filtering by app if given.
        kwargs = {}
        params = request.query_params
        app = params.get('app', None)
        if app:
            kwargs['app'] = app

        level = user.experience.level(**kwargs)
        content = level
        return Response(content)

    @list_route(permission_classes=[IsAuthenticated])
    def status(self, request):
        user = request.user

        # Filtering by app if given.
        kwargs = {}
        params = request.query_params
        app = params.get('app', None)
        if app:
            kwargs['app'] = app

        level = user.experience.level(**kwargs)
        experience = user.experience.total(**kwargs)
        content = {
            'level': level,
            'experience': experience,
            'next': 100
        }
        return Response(content)
