
from django.urls import path, include
from cars.views import car_list, car_details

urlpatterns = [
    path('', car_list),
    path('<int:id>/', car_details),
    ]