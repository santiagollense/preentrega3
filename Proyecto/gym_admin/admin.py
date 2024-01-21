from django.contrib import admin

from . import models

admin.site.register(models.Gym)
admin.site.register(models.Gymbro)
admin.site.register(models.Turno)
admin.site.register(models.Entrenamiento)
admin.site.register(models.Rutina)
admin.site.register(models.Plan)
admin.site.register(models.GymbroporTurno)