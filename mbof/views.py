import os

from rest_framework import viewsets

from .models import Event, User, Vote
from .serializers import EventSerializer, UserSerializer, VoteSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('surname')
    serializer_class = UserSerializer


class CurrentUserViewSet(UserViewSet):
    """
    API endpoint that gives details about the current user.
    """

    def get_queryset(self):
        """
        Defining queryset as a method, because it's required when using dynamic expressions,
        like the value used in `filter()`, which changes with each request.

        :returns: User object which represents the current remote user

        """
        return User.objects.filter(loginName=os.getenv('REMOTE_USER'))


class EventViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows events to be viewed (oldest first) or edited.
    """
    queryset = Event.objects.all().order_by('postingTime')
    serializer_class = EventSerializer


class RecentEventViewSet(EventViewSet):
    """
    API endpoint that allows events to be viewed (newest first) or edited.

    Notice it's a subclass of `EventViewSet`, not `viewsets.ModelViewSet`.
    """
    queryset = Event.objects.all().order_by('-postingTime')


class VoteViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows votes to be viewed or edited.
    """
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer
