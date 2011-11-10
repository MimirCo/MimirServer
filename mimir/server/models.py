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