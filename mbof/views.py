from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404

from .models import Message


def index(request):
    return render(request, 'messages/index.html', {
        'latestMessageList': Message.objects.order_by('-postingTime')[:5],
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
