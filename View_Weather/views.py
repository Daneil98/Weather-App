from django.shortcuts import render
from .weatherapi import get_meta_data
from .forms import Location
from django.http import HttpResponseRedirect
# Create your views here.

def weather_now(request, **location):
    location = request.POST['location']
    return render(request, 'location.html', {'location': location, 'meta': get_meta_data(location)})

def home(request):
    if request.method == 'GET':
        form = Location(request.POST)
        if form.is_valid():
            location = request.POST['location']
            return HttpResponseRedirect('location.html')
        else:
            form = Location()
    return render(request, 'index.html', {'form': form})