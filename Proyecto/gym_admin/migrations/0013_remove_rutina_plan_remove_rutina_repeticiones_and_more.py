# Generated by Django 5.0.1 on 2024-01-25 11:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gym_admin', '0012_remove_gymbroporturno_plan_gymbroporturno_rutina'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rutina',
            name='plan',
        ),
        migrations.RemoveField(
            model_name='rutina',
            name='repeticiones',
        ),
        migrations.RemoveField(
            model_name='rutina',
            name='series',
        ),
        migrations.AddField(
            model_name='gymbro',
            name='addinfo',
            field=models.TextField(blank=True, default='', verbose_name='Información adicional'),
        ),
        migrations.AddField(
            model_name='gymbroporturno',
            name='plan',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='gym_admin.plan'),
        ),
        migrations.AlterField(
            model_name='plan',
            name='plan',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='rutina',
            name='rutina',
            field=models.TextField(default='Ingrese Rutina'),
        ),
    ]
