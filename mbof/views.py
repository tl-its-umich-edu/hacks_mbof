from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets

from .models import Message, User
from .serializers import MessageSerializer, UserSerializer


def index(request):
    return render(request, 'messages/index.html', {
        'latestMessageList': Message.objects.order_by('-postingTime'),
    })


def detail(request, messageId):
    message = get_object_or_404(Message, pk=messageId)
    return render(request, 'messages/detail.html', {
        'message': message,
    })


def results(request, messageId):
    response = "You're looking at the results of message %s."
    return HttpResponse(response % messageId)


def vote(request, messageId):
    return HttpResponse("You're voting on message %s." % messageId)


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('surname')
    serializer_class = UserSerializer


class MessageViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Message.objects.all().order_by('postingTime')
    serializer_class = MessageSerializer
