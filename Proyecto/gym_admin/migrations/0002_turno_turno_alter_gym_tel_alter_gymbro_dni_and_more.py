# Generated by Django 5.0.1 on 2024-01-21 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gym_admin', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='turno',
            name='turno',
            field=models.CharField(blank=True, default='', max_length=10),
        ),
        migrations.AlterField(
            model_name='gym',
            name='tel',
            field=models.CharField(max_length=14),
        ),
        migrations.AlterField(
            model_name='gymbro',
            name='dni',
            field=models.CharField(max_length=9),
        ),
        migrations.AlterField(
            model_name='gymbro',
            name='tel',
            field=models.CharField(max_length=14),
        ),
    ]