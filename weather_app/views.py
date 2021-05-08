import requests
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse


# Create your views here.
def index(request):
    url = "http://api.openweathermap.org/data/2.5/weather?q={city_nm}&appid=8554bee5ea12a558fe029889f3a5808c"
    result = requests.get(url.format(city_nm = "mumbai"))
    return JsonResponse(result.json(), safe = False)
