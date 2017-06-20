from rest_framework import viewsets

from .serializers import CheckpointSerializer
from .models import Checkpoint


class CheckpointViewSet(viewsets.ModelViewSet):
    queryset = Checkpoint.objects.all()
    serializer_class = CheckpointSerializer

    def get_queryset(self):
        user = self.request.user
        return user.checkpoints.all()
