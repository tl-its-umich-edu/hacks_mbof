from rest_framework import serializers

from .models import Message, User


class UserSerializer(serializers.HyperlinkedModelSerializer):
    # url = serializers.HyperlinkedIdentityField(
    #         view_name='user-view-set',
    #         lookup_field='loginName'
    # )

    class Meta:
        model = User
        # FIXME: problem with 'roles' in 'fields'
        fields = ('url', 'loginName', 'displayName',)


class MessageSerializer(serializers.HyperlinkedModelSerializer):
    owner = UserSerializer()

    class Meta:
        model = Message
        fields = ('url', 'messageText', 'latitude', 'longitude', 'altitudeMeters', 'owner', 'postingTime', 'startTime',
                  'endTime',)
