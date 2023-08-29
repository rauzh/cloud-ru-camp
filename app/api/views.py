import socket
import os
from django.http import HttpResponse

def hostname(request):
    return HttpResponse(socket.gethostname())

def author(request):
    author = os.environ.get('AUTHOR', 'Unknown')
    return HttpResponse(author)

def uid(request):
    uid = os.environ.get('UUID', 'Unknown')
    return HttpResponse(uid)

