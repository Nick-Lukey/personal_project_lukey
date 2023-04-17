from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def render_react(request):
    print('home!')
    theInedex = open('static/index.html').read()
    return HttpResponse(theInedex)
