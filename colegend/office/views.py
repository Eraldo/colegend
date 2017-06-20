from rest_framework import viewsets

from .serializers import FocusSerializer
from .models import Focus


class FocusViewSet(viewsets.ModelViewSet):
    queryset = Focus.objects.all()
    serializer_class = FocusSerializer
    filter_fields = ['scope', 'start']

    def get_queryset(self):
        user = self.request.user
        return user.focuses.all()
