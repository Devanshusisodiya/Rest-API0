from django.db import models

# Create your models here.
class User(models.Model):
    api_key = models.CharField(max_length=9)
    name = models.CharField(primary_key=True, max_length=90)
    latitude = models.DecimalField(max_digits=9, decimal_places=4)
    longitude = models.DecimalField(max_digits=9, decimal_places=4)

    def __str__(self):
        return self.name
