from rest_framework import serializers

from .models import InterviewEntry


class InterviewEntrySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = InterviewEntry
        fields = [
            'url', 'id', 'owner',
            'scope', 'start',
            'likes', 'dislikes',
            'created', 'modified',
        ]
        read_only_fields = ['owner']
