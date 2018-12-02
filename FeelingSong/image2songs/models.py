from django.db import models

# Create your models here.

class UserData(models.Model):
    email=models.CharField(max_length=30)
    user=models.CharField(max_length=50)
    name=models.CharField(max_length=20)

    def __unicode__(self):
        return self.name


class Feeling(models.Model):
        score=models.ForeignKey(UserData,on_delete=models.CASCADE)
        field_1=models.IntegerField()
        field_2=models.IntegerField()
        field_3=models.IntegerField()
        field_4=models.IntegerField()
        field_5=models.IntegerField()
        field_6=models.IntegerField()
        field_7=models.IntegerField()

        def __unicode__(self):
            return self.score
