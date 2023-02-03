from django.urls import path
from .views import LoginView
from .views import LogoutView
from .views import WeatherInformationList
from rest_framework import routers
# router = DefaultRouter()
urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
     path('logout/', LogoutView.as_view(), name='logout'),
    #  path('weather/', WeatherInformationList.as_view(), name='weather_information_list'),
     path('weather/', WeatherInformationList.as_view(), name='weather-list'),
]
