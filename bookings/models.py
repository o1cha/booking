from django.db import models
from config import settings


class Booking(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="bookings",
    )
    room = models.ForeignKey(
        "hotels.Room",
        on_delete=models.CASCADE,
        related_name="bookings"
    )
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    status = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
