from django.db import models

# Create your models here.
class Team(models.Model):
    name = models.CharField(max_length=150)
    team_color = models.CharField(max_length=50)
    points = models.IntegerField(default=0)
    logo = models.ImageField(upload_to='logos/')
    car = models.ImageField(upload_to='cars/')

    def __str__(self):
        return self.name
