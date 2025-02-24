from django.shortcuts import render
from django.http import JsonResponse
import requests
import json

def index(request):
    return render(request, 'weather_app/index.html')

def get_weather(request):
    if request.method == 'POST':
        city = request.POST.get('city')
        api_key = 'ddd'  # Replace with your OpenWeatherMap API key
        
        try:
            url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
            response = requests.get(url)
            data = response.json()
            
            if response.status_code == 200:
                weather_data = {
                    'temperature': round(data['main']['temp']),
                    'description': data['weather'][0]['description'].title(),
                    'humidity': data['main']['humidity'],
                    'wind_speed': data['wind']['speed'],
                    'city': data['name'],
                    'status': 'success'
                }
            else:
                weather_data = {'status': 'error', 'message': 'City not found'}
                
            return JsonResponse(weather_data)
            
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)})
    
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'})
