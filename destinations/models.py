from django.db import models

class Destination(models.Model):
    name = models.CharField(max_length=200)
    destinationType = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    activities = models.CharField(max_length=2000)
    imageUrl = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.destinationType + ' : ' + self.name

