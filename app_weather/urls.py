# urls.py in store

from django.urls import path
from .views import view_weather


urlpatterns = [
    path('weather/', view_weather),
]