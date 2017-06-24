from rest_framework import serializers

from .models import Focus


class FocusSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Focus
        fields = [
            'url', 'id', 'owner',
            'scope', 'start',
            'outcome_1', 'outcome_2', 'outcome_3', 'outcome_4',
            'created', 'modified',
        ]
