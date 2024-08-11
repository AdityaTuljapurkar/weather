from django.shortcuts import render
from django.http import HttpResponse
import json
import urllib.request
import urllib.parse

# Create your views here.
def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        city_encoded = urllib.parse.quote(city)  # URL encode the city name
        url = 'http://api.openweathermap.org/data/2.5/weather?q=' + city_encoded + '&id=524901&appid=9e6a625f53ed2717ada64ef87f7650cd'
        res = urllib.request.urlopen(url).read()
        json_data = json.loads(res)
        data = {
            'county_code': str(json_data['sys']['country']),
            'coordinate': str(json_data['coord']['lon']) + ' ' + str(json_data['coord']['lat']),
            'temp': str(json_data['main']['temp']) + 'K',
            'humidity': str(json_data['main']['humidity']),
            'pressure': str(json_data['main']['pressure']),
        }

    else:
        city = ''
        data = {}
    return render(request, 'index.html', {'city':city , 'data':data})
