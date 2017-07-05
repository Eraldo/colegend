from django.contrib.auth.models import Group
from rest_auth.registration.serializers import RegisterSerializer
from rest_framework import serializers
from colegend.users.models import User


class JoinSerializer(RegisterSerializer):
    def validate_username(self, original_username):
        # Add a number until the username does not exist yet.
        username = original_username
        suffix = 2
        while User.objects.filter(username__iexact=username).exists():
            username = original_username + str(suffix)
        return super().validate_username(username)


class OwnedUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = [
            'url', 'id', 'username', 'email', 'name',
            'gender', 'birthday', 'address', 'phone',
            'occupation', 'avatar', 'purpose',
            'date_joined',
            'duo', 'clan', 'tribe',
            'groups', 'is_staff',
            'roles', 'checkpoints'
        ]


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'email', 'name', 'avatar', 'date_joined', 'is_staff')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    user_set = serializers.HyperlinkedRelatedField(many=True, view_name='user-detail', read_only=True)

    class Meta:
        model = Group
        fields = ('url', 'id', 'name', 'user_set')
