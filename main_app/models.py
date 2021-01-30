from django.db import models
from django.urls import reverse
# Create your models here.
TRAINERS = (
    ('1', 'Trainer One'),
    ('2', 'Trainer Two'),
    ('3', 'Trainer Three'),
)

class Pokemon(models.Model):
    name=models.CharField(max_length=50)
    description = models.TextField(max_length=250)
    def __str__(self):
        return self.name