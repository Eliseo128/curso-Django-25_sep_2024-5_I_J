from django.db import models

# Create your models here.

class Templeado(models.Model):
    nombre=models.CharField(max_length=50, blank=True)
    url= models.URLField()
