from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Siema tu nadaje Kosu")
# Create your views here.
