from django.db import models

# Create your models here.
class Video(models.Model):
    title = models.CharField(max_length=100, default='Video')
    category = models.CharField(max_length=100)
    url = models.URLField()

    def __str__(self):
        return self.title