from rest_framework import serializers

from .models import JournalEntry


class JournalEntrySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = JournalEntry
        fields = [
            'url', 'id', 'owner',
            'scope', 'start',
            'content',
            'created', 'modified',
        ]
        read_only_fields = ['owner']
