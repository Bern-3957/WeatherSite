import requests
from django.shortcuts import render, redirect
from .models import City
from .forms import CityForm

# Create your views here.

def index(request):
    appid = 'c7aff2e12a90aea7f666a8928467ffe0'

    if (request.method == 'POST'):
        form = CityForm(request.POST)
        form.save()

    form = CityForm

    cities = City.objects.all()

    all_cities = []

    for city in cities:
        url = f'https://api.openweathermap.org/data/2.5/weather?q={city.name}&lang=ru&units=metric&appid={appid}'
        print(city.name)

        res = requests.get(url).json()
        city_info = {
            'city': city.name,
            'temp': res["main"]["temp"],
            'icon': res["weather"][0]["icon"]

        }

        all_cities.append(city_info)

    context = {
        'all_info': all_cities,
        'form': form,
        'cities': cities
    }

    return render(request, 'weather/index.html', context)



