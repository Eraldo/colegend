from rest_framework import serializers

from .models import Checkpoint


class CheckpointSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Checkpoint
        fields = ['url', 'id', 'name']
