from django.shortcuts import render
from django.contrib import messages
import requests
import datetime
import json
import time

def home(request):
    if request.method == 'POST':
        city = request.POST.get('city')
    else:
        city = 'New Delhi'

    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=70e235e00c7da2c380ca9c6631a51361'

    params = {'units': 'metric'}
    api_key = '70e235e00c7da2c380ca9c6631a51361'

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()

        description = data['weather'][0]['description']
        icon = data['weather'][0]['icon']
        temp = data['main']['temp']
        day = datetime.date.today()

        return render(request, 'weatherapp/index.html', {
            'description': description,
            'icon': icon,
            'temp': temp,
            'day': day,
            'city': city,
            'time' : datetime.datetime.now(),
        })

    except requests.exceptions.RequestException as e:
        day = datetime.date.today()
        messages.error(request, 'City not found!')
        return render(request, 'weatherapp/index.html', {
            'description': 'City not found!',
            'icon': '',
            'temp': '',
            'day': day,
            'city': city,
            'time' : datetime.datetime.now(),
        })
    
def about(request):
    return render(request, 'weatherapp/about.html')

def contact(request):
    return render(request, 'weatherapp/contact.html')