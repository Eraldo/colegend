from rest_framework import serializers

from .models import Outcome


class OutcomeSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.name')

    class Meta:
        model = Outcome
        fields = [
            'url', 'id', 'owner', 'name',
            'description', 'status', 'inbox', 'scope',
            'date', 'deadline', 'estimate',
            'is_focus'
        ]
