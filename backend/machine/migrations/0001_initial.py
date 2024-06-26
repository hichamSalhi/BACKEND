# Generated by Django 5.0.4 on 2024-04-25 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Machine1',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('running_time', models.FloatField()),
                ('planned_production_time', models.FloatField()),
                ('ideal_cycle_time', models.FloatField()),
                ('total_count', models.IntegerField()),
                ('good_count', models.IntegerField()),
                ('availability', models.FloatField()),
                ('performance', models.FloatField()),
                ('quality', models.FloatField()),
                ('Overall_Equipment_Effectiveness', models.FloatField()),
                ('timestamp', models.TextField()),
            ],
            options={
                'db_table': 'machine_1',
            },
        ),
        migrations.CreateModel(
            name='Machine2',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('running_time', models.FloatField()),
                ('planned_production_time', models.FloatField()),
                ('ideal_cycle_time', models.FloatField()),
                ('total_count', models.IntegerField()),
                ('good_count', models.IntegerField()),
                ('availability', models.FloatField()),
                ('performance', models.FloatField()),
                ('quality', models.FloatField()),
                ('Overall_Equipment_Effectiveness', models.FloatField()),
                ('timestamp', models.TextField()),
            ],
            options={
                'db_table': 'machine_2',
            },
        ),
        migrations.CreateModel(
            name='Machine3',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('running_time', models.FloatField()),
                ('planned_production_time', models.FloatField()),
                ('ideal_cycle_time', models.FloatField()),
                ('total_count', models.IntegerField()),
                ('good_count', models.IntegerField()),
                ('availability', models.FloatField()),
                ('performance', models.FloatField()),
                ('quality', models.FloatField()),
                ('Overall_Equipment_Effectiveness', models.FloatField()),
                ('timestamp', models.TextField()),
            ],
            options={
                'db_table': 'machine_3',
            },
        ),
        migrations.CreateModel(
            name='Machine4',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('running_time', models.FloatField()),
                ('planned_production_time', models.FloatField()),
                ('ideal_cycle_time', models.FloatField()),
                ('total_count', models.IntegerField()),
                ('good_count', models.IntegerField()),
                ('availability', models.FloatField()),
                ('performance', models.FloatField()),
                ('quality', models.FloatField()),
                ('Overall_Equipment_Effectiveness', models.FloatField()),
                ('timestamp', models.TextField()),
            ],
            options={
                'db_table': 'machine_4',
            },
        ),
    ]
