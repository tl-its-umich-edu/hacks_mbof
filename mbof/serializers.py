import logging
import os
from curses import has_key

from datetime import datetime, timedelta

import dateutil.parser
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


        postingTime = datetime.utcnow().isoformat()
        self.initial_data[u'postingTime'] = postingTime

        startTime = postingTime
        if (not has_key(self.initial_data, u'startTime')):
            self.initial_data[u'startTime'] = startTime
        else:
            try:
                startTime = dateutil.parser.parse(self.initial_data[u'startTime'])
            except:
                pass

        if (not has_key(self.initial_data, u'endTime')):
            endTime = startTime + timedelta(days=5)
            self.initial_data[u'startTime'] = endTime


        return super(MessageSerializer, self).is_valid(raise_exception)
