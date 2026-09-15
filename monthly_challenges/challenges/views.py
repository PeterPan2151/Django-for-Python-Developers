from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse



challenges = {
    "january":"Celebrate new year",
    "february": "Valentines",
    "march": "My Birthday",
    "april": "April Fools",
    "may": "Diana's Birthday",
    "june": "Vacations",
    "july": "Spring break",
    "august": "Back to school",
    "september": None,
    "octuber": "Halloween",
    "november": "Nothing",
    "december": "Christmas"
}

# Create your views here.
def index(request):
    months = list(challenges.keys())
    return render(request, "challenges/index.html", {
        "months": months
    })



def monthly_challenge_by_number(request, month):
    months = list(challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("Invalid month")
    
    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = challenges[month]
        return render(request, "challenges/challenge.html", {
            "text": challenge_text,
            "month" : month
        })
    except:
        raise Http404()
    
