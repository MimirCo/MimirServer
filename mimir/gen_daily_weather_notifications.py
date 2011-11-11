import setup_environment
import datetime
from server.models import UserWeatherInfo, WeatherInfo, Notification

# Loop over all entries in the UserWeatherInfo table
user_weather_infos = UserWeatherInfo.objects.all()
for user_weather_info in user_weather_infos:
    user_id = user_weather_info.user_id
    location = user_weather_info.location
    # Obtain weather info for this location.
    weather_info = WeatherInfo.objects.get(location=location, date=datetime.date.today())
    notification = 'The weather prediction is %s with a max temperature of %f' % (weather_info.forecast_condition,
                                                                                  weather_info.forecast_temperature)
    tomorrow = datetime.date.today() + datetime.timedelta(days=1)
    morning_time = datetime.time(8, 00)
    tomorrow_time = datetime.datetime.combine(tomorrow, morning_time)
    notif = Notification(user_id=user_id, notification=notification,
                         schedule_time=tomorrow_time, done=False)
    notif.save()