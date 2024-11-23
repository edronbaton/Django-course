from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def january(request):
    return HttpResponse("Январь по английски будет january")


def february(request):
    return HttpResponse("Февраль по английски будет february")