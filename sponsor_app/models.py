from django.db import models

class Sponsorpost(models.Model):
    business_name = models.CharField(max_length=50)
    business_industry = models.CharField(max_length=100)
    about_sponsor = models.TextField()
    budget = models.IntegerField(default=5000)
    email = models.EmailField()
