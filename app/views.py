from django.shortcuts import render

# Create your views here.
from django.contrib.auth import authenticate
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from app.serializers import LoginSerializer,WeatherInformation

class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        username = request.data.get("username", "")
        password = request.data.get("password", "")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            token, created = Token.objects.get_or_create(user=user)
            return Response({"token": token.key}, status=200)
        else:
            return Response({"error": "Invalid credentials"}, status=400)

from django.contrib.auth import logout
from rest_framework import generics
from rest_framework.response import Response

class LogoutView(generics.GenericAPIView):
    def get(self, request, *args, **kwargs):
        logout(request)
        return Response({"message": "Logged out successfully"}, status=200)

from .models import WeatherInformation
from .serializers import WeatherInformationSerializer
from rest_framework import generics

import requests

class WeatherInformationList(generics.ListAPIView):
    queryset = WeatherInformation.objects.all()
    serializer_class = WeatherInformationSerializer

    def get(self, request, *args, **kwargs):
        # List of city names
        cities = ['Delhi','Navi Mumbai','Ahemednagar','Belgaum','Adoni',
        'Ongole','Narasapuram','Hingoli','Virar','Harnai','Aurangabad',
        'Latur','Solapur','Gulbarga','Kolhapur','Raigarth Fort',
        'Dhaka','Bengaluru','Karachi','Bangkok','Budta','Saipan','Manaus',
        'London', 'Paris', 'Berlin', 'New York',]  # 30 city names
        
        # API Key for OpenWeatherMap
        api_key = '4fab66751288ad50a7e03372fb879f84'

        # Iterate over the list of cities
        for city in cities:
            # Construct the API URL
            url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'

            # Make a request to the API
            response = requests.get(url)
            
            # Check if the request was successful
            if response.status_code == 200:
                # Parse the JSON response data
                data = response.json()

                # Extract the weather information from the response data
                city_name = data['name']
                temperature = data['main']['temp']
                humidity = data['main']['humidity']
                pressure = data['main']['pressure']
                wind_speed = data['wind']['speed']
                description = data['weather'][0]['description']
                # i have created this for the infomation purpose to save the data
                # Create a new WeatherInformation object and save it to the database
                # weather_info = WeatherInformation(
                #     city_name=city_name,
                #     temperature=temperature,
                #     humidity=humidity,
                #     pressure=pressure,
                #     wind_speed=wind_speed,
                #     description=description
                # )
                # weather_info.save()
        
        # Call the parent get method to return the weather information
        return super().get(request, *args, **kwargs)
