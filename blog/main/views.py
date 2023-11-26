from django.shortcuts import render
from django.http import HttpResponse
import requests
from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps

def index(request):

    context = {
        'current_temp': get_weather()
    }
    
    return render(request, 'main/index.html', context)



def get_weather():
    owm = OWM('Api key')
    mgr = owm.weather_manager()


    # Search for current weather in London (Great Britain) and get details
    observation = mgr.weather_at_place('Saint Petersburg')
    w = observation.weather

    w.detailed_status         # 'clouds'
    t = w.temperature('celsius')['temp']  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}
    return round(t)




def about(request):
    return render(request, 'main/about.html')
