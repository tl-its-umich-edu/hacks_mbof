from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class User(models.Model):
    loginName = models.CharField(max_length=80)

    def __str__(self):
        return str(self.loginName) + ' (' + self.__class__.__name__ + ': ' + str(self.id) + ')'


@python_2_unicode_compatible
class Message(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    altitudeMeters = models.FloatField()
    messageText = models.CharField(max_length=400)
    postingTime = models.DateTimeField()
    startTime = models.DateTimeField()
    endTime = models.DateTimeField()
    user = models.ForeignKey(User)
    likes = models.IntegerField(default=0)

    def __str__(self):
        return str(self.messageText) + ' (' + self.__class__.__name__ + ': ' + str(self.id) + ')'
