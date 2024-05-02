from django.db import models

class Machine(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    class Meta:
        db_table = 'machine'  # Set the table name if it differs from the model name
        app_label = 'maintenance'  # Specify the app label if necessary


class MaintenanceType(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    class Meta:
        db_table = 'maintenance_type'  # Set the table name if it differs from the model name
        app_label = 'maintenance'  # Specify the app label if necessary

class Maintenance(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.TextField()
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE)
    maintenance_type = models.ForeignKey(MaintenanceType, on_delete=models.CASCADE)
    start = models.DateTimeField()
    end = models.DateTimeField()
    description = models.TextField()

    class Meta:
        db_table = 'maintenance'  # Set the table name if it differs from the model name
        app_label = 'maintenance'  # Specify the app label if necessary