from django.shortcuts import render

# views.py
from rest_framework import generics
from .models import Maintenance, Machine, MaintenanceType
from .serializers import MaintenanceSerializer, MachineSerializer, MaintenanceTypeSerializer

class MaintenanceListAPIView(generics.ListAPIView):
    queryset = Maintenance.objects.all()
    serializer_class = MaintenanceSerializer

class MachineListAPIView(generics.ListAPIView):
    queryset = Machine.objects.all()
    serializer_class = MachineSerializer

# API's for maintenance
class MaintenanceTypeListAPIView(generics.ListAPIView):
    queryset = MaintenanceType.objects.all()
    serializer_class = MaintenanceTypeSerializer

class MaintenanceCreateAPIView(generics.CreateAPIView):
    queryset = Maintenance.objects.all()
    serializer_class = MaintenanceSerializer

class MaintenanceDestroyAPIView(generics.DestroyAPIView):
    queryset = Maintenance.objects.all()
    serializer_class = MaintenanceSerializer