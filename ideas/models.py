from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class IdeasModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="Contributor_post")
    Title = models.CharField(max_length=150)
    About_contributor = models.CharField(max_length=200)
    Idea_industry = models.CharField(max_length=100)
    Idea_text = models.TextField()
    Budget = models.PositiveIntegerField(default=0)
    Contact_email = models.EmailField()

    def __str__(self):
        return self.Title

    def get_absolute_url(self):
        return reverse('ideas_detail', args=[str(self.id)])

