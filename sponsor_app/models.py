from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator




class Sponsorpost(models.Model):
    business_name = models.CharField(max_length=50)
    about_sponsor = models.TextField()
    business_industry = models.CharField(max_length=100)
    budget = models.IntegerField(validators=[MinValueValidator(1000), MaxValueValidator(500000)], default=5000)
    email = models.EmailField()

