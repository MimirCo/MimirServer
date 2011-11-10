from django.db import models

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    device_token = models.CharField(max_length=64)
  
    def __unicode__(self):
        return u'%d %s' % (self.user_id, self.device_token)  

class Notification(models.Model):
    user_id = models.IntegerField()
    notification = models.CharField(max_length=256)
    schedule_time = models.DateTimeField()
    done = models.BooleanField()
    
    def __unicode__(self):
        return self.notification

class UserWeatherInfo(models.Model):
    user_id = models.IntegerField()
    location = models.CharField(max_length=200)
    time_zone = models.IntegerField()
    
    def __unicode__(self):
        return u'%s %d' % (self.location, self.time_zone)
    
class WeatherInfo(models.Model):
    location = models.CharField(max_length=200)
    date = models.DateField()
    time = models.TimeField()
    temperature = models.FloatField()
    condition = models.CharField(max_length=200)
    forecast_temperature = models.FloatField()
    forecast_condition = models.CharField(max_length=200)
    
    def __unicode__(self):
        return u'location: %s, temperature: %f, condition: %s' % (self.location,
                                                                  self.temperature,
                                                                  self.condition)