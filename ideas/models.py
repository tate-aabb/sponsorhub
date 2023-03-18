from django.db import models
from django.contrib.auth.models import User

class IdeasModel(models.Model):
    About_contributing = models.CharField(max_length=200)
    Idea_industry = models.CharField(max_length=100)
    Idea_text = models.TextField()
    Budget = models.PositiveIntegerField()
    Contact_email = models.EmailField(default=0)
# Create your models here.
