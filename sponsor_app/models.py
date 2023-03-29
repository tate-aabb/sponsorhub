from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
class Sponsorpost(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="Sponsor_post")
    business_name = models.CharField(max_length=50)
    business_industry = models.CharField(max_length=100)
    about_sponsor = models.TextField()
    budget = models.IntegerField(default=5000)
    email = models.EmailField()

    def __str__(self):
        return self.business_name

    def get_absolute_url(self):
        return reverse("sponsor_detail", args=[str(self.id)])
