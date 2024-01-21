# Generated by Django 5.0.1 on 2024-01-21 20:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gym_admin', '0006_remove_gymbroporturno_rutina_gymbroporturno_plan_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gymbroporturno',
            name='plan',
        ),
        migrations.AddField(
            model_name='gymbroporturno',
            name='rutina',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='gym_admin.rutina'),
        ),
    ]
