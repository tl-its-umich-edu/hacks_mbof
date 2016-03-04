import logging

from rest_framework import serializers

from .models import Message, User, Vote

logger = logging.getLogger(__name__)


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        # FIXME: problem with 'roles' in 'fields'
        fields = ('url', 'loginName', 'displayName', 'aboutMe',)


class MessageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Message
        fields = ('url', 'messageText', 'latitude', 'longitude', 'altitudeMeters', 'owner', 'postingTime', 'startTime',
                  'endTime',)

class VoteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Vote
        fields = ('vote','voter','message')