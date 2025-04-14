from django_filters import FilterSet
from .models import Car
import django_filters


class CarFilter(FilterSet):
   class Meta:

       model = Car

       fields = {'vin': ['icontains'],
           'vehicle_model': ['exact'],
           'engine_model': ['exact'],
           'drive_axle_number': ['icontains'] }