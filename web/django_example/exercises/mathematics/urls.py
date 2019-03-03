from django.contrib import admin
from django.urls import path

from greetings.views import hello_world, hello_name
from mathematics.views import funkcje_matematyczne

urlpatterns = [
    path('math/<operation>/<liczba1>/<liczba2>', funkcje_matematyczne),
]