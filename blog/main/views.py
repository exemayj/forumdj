from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    data = {
        'title':'Main page',
    }
    return render(request, 'main/index.html',)

def about(request):
    return render(request, 'main/about.html')

def profile(request):
    return render(request, 'main/profile.html')