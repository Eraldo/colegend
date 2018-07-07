from rest_framework import serializers

from .models import Role


class RoleSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Role
        fields = ['url', 'id', 'name', 'nickname', 'item', 'icon', 'metrics']
