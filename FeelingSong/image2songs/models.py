from django.db import models
from django.contrib.auth.models import User
from django.db.models import DateTimeField
# Create your models here.


class Feeling(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    datetime = models.DateTimeField()
    happiness = models.FloatField()
    anger = models.FloatField()
    neutral = models.FloatField()
    sadness = models.FloatField()
    fear = models.FloatField()
    surprise = models.FloatField()
    disgust = models.FloatField()

    def __unicode__(self):
        return self.username
