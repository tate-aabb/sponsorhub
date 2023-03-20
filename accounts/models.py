from django.db import models
from django.contrib.auth.models import User

class Type(models.IntegerChoices):
    SPONSOR = 0, "Sponsor"
    CONTRIBUTOR = 1, "Contributor"

class CustomUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    user_type = models.IntegerField(choices=Type.choices, default=Type.SPONSOR)

