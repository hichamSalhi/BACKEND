# urls.py
from django.urls import path
from .views import MaintenanceListAPIView, MachineListAPIView, MaintenanceTypeListAPIView, MaintenanceDestroyAPIView, MaintenanceCreateAPIView

urlpatterns = [
    path('getAll/', MaintenanceListAPIView.as_view(), name='maintenance-list'),
    path('getMachines/', MachineListAPIView.as_view(), name = 'machine-list'),
    path('getMaintenanceType/', MaintenanceTypeListAPIView.as_view(), name='maintenance-type-list'),
    path('deleteMaintenance/<int:pk>/', MaintenanceDestroyAPIView.as_view(), name='maintenance-type-delete'),
    path('AddMaintenance/', MaintenanceCreateAPIView.as_view(), name='maintenance-create'),

]