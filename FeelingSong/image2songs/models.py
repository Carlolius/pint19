from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Feeling(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    datetime = models.CharField(max_length=200)
    happiness = models.IntegerField()
    anger = models.IntegerField()
    neutral = models.IntegerField()
    sadness = models.IntegerField()
    fear = models.IntegerField()
    surprise = models.IntegerField()
    disgust = models.IntegerField()

    def __unicode__(self):
        return self.username
