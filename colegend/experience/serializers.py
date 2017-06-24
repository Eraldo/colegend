from rest_framework import serializers

from .models import Experience


class ExperienceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Experience
        fields = [
            'url', 'id', 'owner',
            'app', 'level', 'amount',
            'created',
        ]
