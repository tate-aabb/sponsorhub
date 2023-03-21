from django.db import models
from django.contrib.auth.models import User

class IdeasModel(models.Model):
    Title = models.CharField(max_length=150)
    About_contributor = models.CharField(max_length=200)
    Idea_industry = models.CharField(max_length=100)
    Idea_text = models.TextField()
    Budget = models.PositiveIntegerField(default=0)
    Contact_email = models.EmailField()
# Create your models here.
