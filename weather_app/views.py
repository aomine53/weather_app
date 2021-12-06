import requests
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.contrib import messages


# Create your views here.
def index(request):
    if request.method == 'POST':
        # print(request.POST)
        url = "http://api.openweathermap.org/data/2.5/weather?q={city_nm}&appid=8554bee5ea12a558fe029889f3a5808c&units=metric"
        city = request.POST['city']     

        # if city.isnumeric():

        result = requests.get(url.format(city_nm = city))
        result = result.json()
        # print(result.json())
        
        cod = result['cod']
        print(cod)
        if cod != 200:
            print("Invalid input")
            return render(request, 'index.html')

        args = {}
        args['name'] = result['name']
        # args['country'] = result['sys']['country']
        args['id'] = result['weather'][0]['id']
        args['desc'] = result['weather'][0]['description']
        args['temp'] = result['main']['temp']
        args['temp_max'] = result['main']['temp_max']
        args['temp_min'] = result['main']['temp_min']
        # print(args)
        messages.success(request,"Searching...")
        # return JsonResponse(result, safe = False)
        return render(request, 'index.html', args)
    else:
        return render(request, 'index.html')