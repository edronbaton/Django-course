from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
# Create your views here.

def january(request):
    return HttpResponse("Январь по английски будет january")


def february(request):
    return HttpResponse("Февраль по английски будет february")

def monthly_challenges(request, month):
    challenge_text = None

    if month == 'january':
        challenge_text = "Не есть мясо целый месяц"
    elif month == 'february':
        challenge_text = "Пробежка по утрам"
    else:
        return HttpResponseNotFound("Этот месяц не поддерживается")
    
    return HttpResponse(challenge_text)