import requests
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse


# Create your views here.
def index(request):
    url = "http://api.openweathermap.org/data/2.5/weather?q={city_nm}&appid=8554bee5ea12a558fe029889f3a5808c&units=metric"
    result = requests.get(url.format(city_nm = "Mumbai"))
    result = result.json()
    # print(result.json())
    args = {}
    args['name'] = result['name']
    args['desc'] = result['weather'][0]['description']
    args['temp'] = result['main']['temp']
    args['temp_max'] = result['main']['temp_max']
    args['temp_min'] = result['main']['temp_min']
    print(args)
    # return JsonResponse(result, safe = False)
    return render(request, 'index.html', args)