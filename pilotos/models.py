from django.db import models
from equipos.models import Team

# Create your models here.
class Pilot(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    points = models.IntegerField()
    flag = models.ImageField(upload_to='banderas')
    photo = models.ImageField(upload_to='pilotos')

    def __str__(self):
        return self.name