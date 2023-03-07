from django.shortcuts import render
import requests
import datetime

def index(request):
     if 'city' in request.POST:
          city = request.POST['city']
     else:
          city = 'perth'

     appid = '0ef93c007badec8df6922fa5b30bc4fd'
     URL = 'https://api.openweathermap.org/data/2.5/weather'
     PARAM = {'q': city, 'appid': appid, 'units': 'metric'}

     r = requests.get(url=URL, params=PARAM)
     res = r.json()

     description = res['weather'][0]['description']
     icon = res['weather'][0]['icon']
     temp = res['main']['temp']
     day = datetime .date.today()


     return render(request, 'weatherapp/index.html', {'description': description,
     'icon':icon, 'temp':temp, 'day':day ,  'city':city })
