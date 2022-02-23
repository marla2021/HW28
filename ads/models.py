from django.db import models


class Location(models.Model):
    name = models.CharField(max_length=30)
    lat = models.FloatField()
    lng = models.FloatField()

    class Meta:
        verbose_name = "Локация"
        verbose_name_plural = "Локации"

    def __str__(self):
        return self.name




# Create your models here.
