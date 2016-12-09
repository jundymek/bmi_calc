from django.db import models


class Bmi(models.Model):
    bmi = models.FloatField()
    counter = models.IntegerField(default=1)
