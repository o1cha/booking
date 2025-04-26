from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, permissions
from rest_framework import filters


from .filters import RoomFilter
from .models import Hotel, Room, Booking

from .permissions import IsAdminOrReadOnly
from .serializers import HotelSerializer, RoomSerializer, BookingSerializer


class HotelsViewSet(viewsets.ModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer
    # Следующая строчка, если закоментировать, отключает требование авторизации
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    permission_classes = (IsAdminOrReadOnly, )


class RoomsViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_class = RoomFilter
    ordering_fields = ['price_per_night']
    ordering = ['price_per_night']
    permission_classes = (IsAdminOrReadOnly,)


class BookingsViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
