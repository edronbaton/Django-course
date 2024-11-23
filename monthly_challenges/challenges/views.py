from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

monthly_challenges = {
    "january": "Не есть мясо целый месяц!",
    "february": "Гулять как минимум по 20 минут в день!",
    "march": "Выпивать не менее 2 литров воды каждый день!",
    "april": "Просыпаться на час раньше обычного!",
    "may": "Медитировать каждый день хотя бы по 10 минут!",
    "june": "Заниматься спортом 4 раза в неделю!",
    "july": "Не есть сахар в течение месяца!",
    "august": "Читать как минимум 10 страниц книги каждый день!",
    "september": "Пробовать каждую неделю что-то новое (блюдо, место, хобби)!",
    "october": "Ограничить время в соцсетях до 1 часа в день!",
    "november": "Писать 3 вещи, за которые ты благодарен, каждый день!",
    "december": "Помогать окружающим (добрые дела, волонтерство или поддержка)!"
}
# Create your views here.

def monthly_challenges_by_name(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound("Этот месяц не поддерживается")
    
    