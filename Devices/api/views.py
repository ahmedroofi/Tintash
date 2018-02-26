from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import rest_framework as filters
from Devices.api.serializer import *


class DeviceFilter(filters.FilterSet):
    assigned__assign_to__isnull = \
     filters.BooleanFilter(name='assigned__assign_to', lookup_expr='isnull')

    class Meta:
        model = Device
        fields = ('assigned__assign_to', 'assigned__assign_to__isnull', 'type',
                  'model', 'identifier',
                  'serial_number', 'year', 'specs', 'vendor_name',
                  'purchase_date', 'purchase_condition', 'inchs', 'sim_number',
                  'whose_name')


# Create your views here.
class DeviceView(viewsets.ModelViewSet):
    serializer_class = DeviceSerializer
    queryset = Device.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filter_class = DeviceFilter


class DeviceTypeView(viewsets.ModelViewSet):

    serializer_class = DeviceTypeSerializer
    queryset = DeviceType.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('name',)
