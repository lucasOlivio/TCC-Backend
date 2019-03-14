from django.contrib.auth.models import User, Group
from rest_framework import serializers

# The serializer is a library to convert the complex types like psql results into json and vice versa
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')