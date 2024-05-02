from rest_framework import serializers
from .models import Maintenance, Machine, MaintenanceType

class MaintenanceSerializer(serializers.ModelSerializer):
    start = serializers.DateTimeField(format="%Y-%m-%dT%H:%M:%S")
    end = serializers.DateTimeField(format="%Y-%m-%dT%H:%M:%S")

    class Meta:
        model = Maintenance
        fields = ['id', 'title', 'start', 'end', 'description', 'machine', 'maintenance_type']

class MachineSerializer(serializers.ModelSerializer):
    class Meta :
        model = Machine
        fields = '__all__'

class MaintenanceTypeSerializer(serializers.ModelSerializer):
    class Meta :
        model = MaintenanceType
        fields = '__all__'