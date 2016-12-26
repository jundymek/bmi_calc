from django.db import models


class Bmi(models.Model):
    bmi = models.FloatField()
    counter = models.IntegerField(default=1)


class Localization(models.Model):
    bmi = models.FloatField()
    ip = models.CharField(max_length=40)
