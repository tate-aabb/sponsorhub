from django.db import models


class ForbesList(models.Model):
    rank = models.IntegerField()
    name = models.CharField(max_length=200)
    net_worth = models.CharField(max_length=200)
    age = models.IntegerField()
