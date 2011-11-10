import setup_environment
import urllib2, simplejson, datetime
from server.models import UserWeatherInfo, WeatherInfo

# Obtain all distinct locations
locations = UserWeatherInfo.objects.values('location').distinct()

for location in locations:
    loc = location['location']
    # Obtain weather info for this loc
    url = 'http://api.wunderground.com/api/ee55837995b62142/geolookup/conditions/forecast/q/%s.json' % (loc)
    f = urllib2.urlopen(url)
    json_string = f.read()
    parsed_json = simplejson.loads(json_string)
    # Obtain current weather info
    current_observation = parsed_json['current_observation']
    temperature = current_observation['temp_f']
    condition = current_observation['weather']
    # Obtain observation time
    epoch_time = current_observation['observation_epoch']
    obs_date = datetime.datetime.fromtimestamp(int(epoch_time)).date()
    obs_time = datetime.datetime.fromtimestamp(int(epoch_time)).time()
    # Obtain forecast info
    simple_forecast = parsed_json['forecast']['simpleforecast']['forecastday'][0]
    # Forecast temperature = high forecast temperature
    forecast_temperature = simple_forecast['high']['fahrenheit']
    forecast_condition = simple_forecast['conditions']
    
    # Create new weather info entry
    weather_info = WeatherInfo(location=loc, date=obs_date, time=obs_time,
                               temperature=temperature, condition=condition,
                               forecast_temperature=forecast_temperature,
                               forecast_condition=forecast_condition)
    weather_info.save() 