from django.contrib.auth.models import User
from rest_framework import serializers



class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')
        extra_kwargs = {'password': {'write_only': True}}


from .models import WeatherInformation

class WeatherInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeatherInformation
        fields = ( 'city_name', 'temperature', 'humidity', 'pressure', 'wind_speed', 'description')


