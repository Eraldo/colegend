from django.contrib.auth.models import Group
from rest_framework import serializers
from colegend.users.models import User


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'email', 'name', 'groups', 'is_staff')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    user_set = serializers.HyperlinkedRelatedField(many=True, view_name='user-detail', read_only=True)

    class Meta:
        model = Group
        fields = ('url', 'id', 'name', 'user_set')
