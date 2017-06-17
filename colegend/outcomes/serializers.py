from rest_framework import serializers

from .models import Outcome


class OutcomeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Outcome
        fields = (
            'url', 'id', 'owner', 'name',
            'description', 'status', 'inbox', 'scope',
            'date', 'deadline', 'estimate'
        )
