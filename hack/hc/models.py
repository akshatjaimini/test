from django.db import models

# Create your models here.
class Sups(models.Model):

    un = models.CharField(max_length=1000)
    p = models.CharField(max_length=1000)
