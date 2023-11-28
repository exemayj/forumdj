from django.shortcuts import render
from django.http import HttpResponse
import requests
from pyowm import OWM
from translate import Translator

def index(request):

    context = {
        'current_temp': get_weather(),
        'current_status': get_weather1(),
    }
    
    return render(request, 'main/index.html', context)



def get_weather():
    owm = OWM('39adf2a129e3475f7055c32a84a08296')
    mgr = owm.weather_manager()

    observation = mgr.weather_at_place('Saint Petersburg')
    w = observation.weather

    t = w.temperature('celsius')['temp']  
    return round(t)
    

def get_weather1():
    owm = OWM('39adf2a129e3475f7055c32a84a08296')
    mgr = owm.weather_manager()

    observation = mgr.weather_at_place('Saint Petersburg')
    w = observation.weather

    s = w.detailed_status
    st = Translator(from_lang="en",to_lang="ru")
    translation = st.translate(s)
    return translation


def about(request):
    return render(request, 'main/about.html')
