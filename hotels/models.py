from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Hotel(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    city = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    rating = models.DecimalField(
        max_digits=2,
        decimal_places=1,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(5),
        ],
    )
    created_at = models.DateTimeField(auto_now_add=True)
