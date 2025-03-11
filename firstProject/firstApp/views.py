from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.
def display(request):
    return HttpResponse('<h1>My First Django App</h1>')

def displayDateTime(request):
    dt = datetime.datetime.now()
    s = f'<b>Current Date and Time: {dt}</b>'
    return HttpResponse(s)