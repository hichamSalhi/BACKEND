# models.py
from django.db import models

class AData(models.Model):
    id = models.AutoField(primary_key=True)
    SensorID = models.TextField()
    Date_n_Time = models.TextField()
    A = models.TextField()

    class Meta:
        db_table = 'A_Data'  # Set the table name if it differs from the model name
        app_label = 'sensor'  # Specify the app label if necessary

class BData(models.Model):
    id = models.AutoField(primary_key=True)
    SensorID = models.TextField()
    Date_n_Time = models.TextField()
    B = models.TextField()

    class Meta:
        db_table = 'B_Data'  # Set the table name if it differs from the model name
        app_label = 'sensor'  # Specify the app label if necessary

class WData(models.Model):
    id = models.AutoField(primary_key=True)
    SensorID = models.TextField()
    Date_n_Time = models.TextField()
    W = models.TextField()

    class Meta:
        db_table = 'W_Data'  # Set the table name if it differs from the model name
        app_label = 'sensor'  # Specify the app label if necessary

class XData(models.Model):
    id = models.AutoField(primary_key=True)
    SensorID = models.TextField()
    Date_n_Time = models.TextField()
    X = models.TextField()

    class Meta:
        db_table = 'X_Data'  # Set the table name if it differs from the model name
        app_label = 'sensor'  # Specify the app label if necessary

class YData(models.Model):
    id = models.AutoField(primary_key=True)
    SensorID = models.TextField()
    Date_n_Time = models.TextField()
    Y = models.TextField()

    class Meta:
        db_table = 'Y_Data'  # Set the table name if it differs from the model name
        app_label = 'sensor'  # Specify the app label if necessary

class ZData(models.Model):
    id = models.AutoField(primary_key=True)
    SensorID = models.TextField()
    Date_n_Time = models.TextField()
    Z = models.TextField()

    class Meta:
        db_table = 'Z_Data'  # Set the table name if it differs from the model name
        app_label = 'sensor'  # Specify the app label if necessary