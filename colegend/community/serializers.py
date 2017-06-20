from rest_framework import serializers

from .models import Duo, Clan, Tribe


class DuoSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Duo
        fields = ['url', 'id', 'name', 'members']


class ClanSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Clan
        fields = ['url', 'id', 'name', 'members']


class TribeSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Tribe
        fields = ['url', 'id', 'name', 'members']
