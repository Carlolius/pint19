from django.db import models

# Create your models here.


class Feeling(models.Model):
    username = models.CharField(max_length=100)
    happiness = models.IntegerField()
    anger = models.IntegerField()
    neutral = models.IntegerField()
    sadness = models.IntegerField()
    fear = models.IntegerField()
    surprise = models.IntegerField()
    disgust = models.IntegerField()

    def __unicode__(self):
        return self.username
