from django.db import models
from django.contrib.auth.models import User

class IdeasModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=User)
    About_contributing = models.CharField(max_length=200)
    Idea_industry = models.CharField(max_length=100)
    Idea_text = models.TextField()
    Budget = models.PositiveIntegerField()
    Contact_email = models.EmailField(default=0)
# Create your models here.

