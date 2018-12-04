from django.db import models

# Create your models here.

class UserData(models.Model):
    email=models.CharField(max_length=30)
    user=models.CharField(max_length=50)
    name=models.CharField(max_length=20)
    token_s=models.CharField(max_length=50)

    def __unicode__(self):
        return self.name


class Feeling(models.Model):
        email=models.ForeignKey(UserData,on_delete=models.CASCADE)
        happiness=models.IntegerField()
        anger=models.IntegerField()
        neutral=models.IntegerField()
        sadness=models.IntegerField()
        fear=models.IntegerField()
        surprise=models.IntegerField()
        disgust=models.IntegerField()

        def __unicode__(self):
            return self.email
