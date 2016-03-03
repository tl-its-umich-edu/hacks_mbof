import logging
import os

from rest_framework import serializers

from .models import Message, User

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

    def is_valid(self, raise_exception=False):
        # FIXME: This method of setting the owner URL seems hackish.  Find the right way.
        self.initial_data[u'owner'] = u'http://localhost:18000/api/users/%s/' % os.getenv('REMOTE_USER')
        return super(MessageSerializer, self).is_valid(raise_exception)
