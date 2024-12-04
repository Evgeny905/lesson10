from django.db import models

# Create your models here.
class Buyer(models.Model):
    name = models.CharField(max_length=100)
    balance = models.DecimalField(decimal_places=10, max_digits=1000)
    age = models.IntegerField()
class Game(models.Model):
    title = models.CharField(max_length=100)
    cost = models.DecimalField(decimal_places=10, max_digits=1000)
    size = models.DecimalField(decimal_places=10, max_digits=1000)
    description = models.TextField()
    age_limited = models.BooleanField(default=False)
    buyer = models.ManyToManyField(Buyer, related_name='games')
    DecimalField = models.DecimalField(decimal_places=10, max_digits=1000)
    BooleanField = models.BooleanField()