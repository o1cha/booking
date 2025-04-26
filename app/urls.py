from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter

from .views import HotelsViewSet, RoomsViewSet, BookingsViewSet


router = DefaultRouter()
router.register('hotels', HotelsViewSet)
router.register('rooms', RoomsViewSet)
router.register('bookings', BookingsViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path(r'api/v1/auth/', include('djoser.urls')),
    re_path(r'auth/', include('djoser.urls.authtoken')),
]
