from rest_framework import serializers

from .models import JournalEntry


class JournalEntrySerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.name')

    class Meta:
        model = JournalEntry
        fields = [
            'url', 'id', 'owner',
            'scope', 'start',
            'created', 'modified',
        ]
