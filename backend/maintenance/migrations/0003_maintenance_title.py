# Generated by Django 5.0.4 on 2024-04-30 16:33

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maintenance', '0002_machine_alter_maintenance_machine'),
    ]

    operations = [
        migrations.AddField(
            model_name='maintenance',
            name='title',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
