from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

# funkcja zwana w django widok
def hello_world(request):
    return HttpResponse("hello world")

def hello_name(request, name):
    return HttpResponse(f"Hello {name}")
