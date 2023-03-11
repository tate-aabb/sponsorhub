from django.db import models


class ForbesList(models.Model):
    rank = models.IntegerField()
    name = models.CharField(max_length=200)
    net_worth = models.CharField(max_length=200)
    age = models.IntegerField()


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.name
