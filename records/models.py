from django.db import models
from django.utils import timezone
from django.urls import reverse
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
    is_available = models.BooleanField(default=True)
    price = models.IntegerField(default=0)
    #image
    # other_info_from_readme


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('records:index')
