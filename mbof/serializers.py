from rest_framework import serializers

from .models import Message, User


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        # FIXME: problem with 'roles' in 'fields'
        fields = ('url', 'loginName', 'displayName',)


class MessageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Message
        fields = ('url', 'messageText', 'latitude', 'longitude', 'altitudeMeters', 'postingTime', 'startTime',
                  'endTime',)
