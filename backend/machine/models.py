from django.db import models

# Create your models here.

class Machine1(models.Model):
    id = models.AutoField(primary_key=True)
    running_time = models.FloatField()
    planned_production_time = models.FloatField()
    ideal_cycle_time = models.FloatField()
    total_count = models.IntegerField()
    good_count = models.IntegerField()
    availability = models.FloatField()
    performance = models.FloatField()
    quality = models.FloatField()
    Overall_Equipment_Effectiveness = models.FloatField()
    timestamp = models.TextField()

    class Meta:
        db_table = 'machine_1'  # Set the table name if it differs from the model name
        app_label = 'machine'  # Specify the app label if necessary

class Machine2(models.Model):
    id = models.AutoField(primary_key=True)
    running_time = models.FloatField()
    planned_production_time = models.FloatField()
    ideal_cycle_time = models.FloatField()
    total_count = models.IntegerField()
    good_count = models.IntegerField()
    availability = models.FloatField()
    performance = models.FloatField()
    quality = models.FloatField()
    Overall_Equipment_Effectiveness = models.FloatField()
    timestamp = models.TextField()

    class Meta:
        db_table = 'machine_2'  # Set the table name if it differs from the model name
        app_label = 'machine'  # Specify the app label if necessary

class Machine3(models.Model):
    id = models.AutoField(primary_key=True)
    running_time = models.FloatField()
    planned_production_time = models.FloatField()
    ideal_cycle_time = models.FloatField()
    total_count = models.IntegerField()
    good_count = models.IntegerField()
    availability = models.FloatField()
    performance = models.FloatField()
    quality = models.FloatField()
    Overall_Equipment_Effectiveness = models.FloatField()
    timestamp = models.TextField()

    class Meta:
        db_table = 'machine_3'  # Set the table name if it differs from the model name
        app_label = 'machine'  # Specify the app label if necessary

class Machine4(models.Model):
    id = models.AutoField(primary_key=True)
    running_time = models.FloatField()
    planned_production_time = models.FloatField()
    ideal_cycle_time = models.FloatField()
    total_count = models.IntegerField()
    good_count = models.IntegerField()
    availability = models.FloatField()
    performance = models.FloatField()
    quality = models.FloatField()
    Overall_Equipment_Effectiveness = models.FloatField()
    timestamp = models.TextField()

    class Meta:
        db_table = 'machine_4'  # Set the table name if it differs from the model name
        app_label = 'machine'  # Specify the app label if necessary