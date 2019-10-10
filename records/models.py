from django.db import models

# Create your models here.

class Records(models.Model):

    MINT = 'MINT'
    LIGHT = 'LIGHTLY'
    AVG = 'AVERAGE'
    HEAVY = 'HEAVILY'

    CONDITION_CHOICES = [
        (MINT, 'Mint'),
        (LIGHT, 'Light'),
        (AVG, 'Average'),
        (HEAVY, 'Heavy'),
    ]

    name = models.CharField(max_length=50)
    condition = models.CharField(max_length=10, choices=CONDITION_CHOICES, default = AVG)


    def __str__(self):
        return self.name
