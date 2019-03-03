from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def funkcje_matematyczne(request, operation, liczba1, liczba2):
    result = None
    liczba1, liczba2 = int(liczba1), int(liczba2)
    if operation == "add":
        result = liczba1 + liczba2
    elif operation == "sub":
        result = liczba1 - liczba2
    elif operation == "mul":
        result = liczba1 * liczba2
    elif operation == "div":
        if liczba2 == 0:
            result = "Nie dziel przez 0"
        else:
            result = liczba1 / liczba2
    return HttpResponse(f"Wynik: {result}")