from django.contrib.auth.models import User
from django.db import models


class Hotel(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    # требуется добавление - адресов.
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Room(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    room_type = models.CharField(max_length=100)
    room_number = models.PositiveIntegerField()
    description = models.TextField()
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    capacity = models.PositiveIntegerField()

    def __str__(self):
        return f"Room {self.room_number} ({self.room_type}) at {self.hotel.title}"


class Booking(models.Model):
    # id отеля
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    # id комнаты
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    # id пользователя
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    guest_count = models.PositiveIntegerField()

    def __str__(self):
        return f"Reservation for {self.user.username}: {self.room}"
