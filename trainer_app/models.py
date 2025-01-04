from django.db import models
from django.core.validators import MaxValueValidator

# Create your models here.

class Trainer(models.Model):
    name = models.CharField(max_length=255)

    age = models.IntegerField()

    def __str__(self):
        return f'Trainer: {self.name}'
    