from django.db import models

# Create your models here.
class Thing(models.Model):
    name = models.CharField(max_length=30, unique=True, blank=False)
    description = models.CharField(max_length=120, unique=False)
    quantity = models.IntegerField(unique=False)
