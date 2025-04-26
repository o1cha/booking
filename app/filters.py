import django_filters
from django.db.models import Q

from .models import Room


class RoomFilter(django_filters.FilterSet):
    capacity = django_filters.NumberFilter(lookup_expr='gte')
    check_in_date = django_filters.DateFilter(method='filter_exclude_dates', label='check-in')
    check_out_date = django_filters.DateFilter(method='filter_exclude_dates', label='check-out')

    class Meta:
        model = Room
        fields = ['capacity']

    def filter_exclude_dates(self, queryset, name, value):
        # If both dates are provided, apply the combined exclude
        if 'check_in_date' in self.data and 'check_out_date' in self.data:
            check_in_date_value = self.data['check_in_date']
            check_out_date_value = self.data['check_out_date']
            return queryset.exclude(
                Q(booking__check_out_date__gt=check_in_date_value) &
                Q(booking__check_in_date__lt=check_out_date_value)
            )
        # If only one of the dates is provided, no need to exclude based on that
        return queryset
