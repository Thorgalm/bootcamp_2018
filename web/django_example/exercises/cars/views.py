from django.shortcuts import render

# Create your views here.

from cars.models import Car

def car_list(request):
    cars = Car.objects.filter(is_ready=True)
    return render(
        request=request,
        template_name="car_list.html",
        context={'cars':cars}
        )

def car_details(request, id):
    car = Car.objects.get(pk=id)
    return render(
        request=request,
        template_name="car_details.html",
        context={'car': car}

    )
