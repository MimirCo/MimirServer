from django.contrib import admin
from server.models import User, Notification, UserWeatherInfo, WeatherInfo

admin.site.register(User)
admin.site.register(Notification)
admin.site.register(UserWeatherInfo)
admin.site.register(WeatherInfo)