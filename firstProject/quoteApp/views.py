from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def displaeyQuote(request):
    return HttpResponse('The best investment we cn make is in ourself')
