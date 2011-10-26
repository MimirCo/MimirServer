from django.db import models

class User(models.Model):
  udid = models.CharField(max_length=200)
