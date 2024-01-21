from django.db import models

class Gym(models.Model):
    nombre = models.CharField(max_length=100)
    dir = models.CharField(max_length=200)
    tel = models.CharField(max_length=14)
    email = models.EmailField()

    def __str__(self):
        return self.nombre

class Gymbro(models.Model):
    nombre = models.CharField(max_length=100)
    dni = models.CharField(max_length=9)
    dir = models.CharField(max_length=200)
    tel = models.CharField(max_length=14)
    email = models.EmailField()
    os = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
    
class Turno(models.Model):
    turno = models.CharField(max_length=10, default='', blank=True)
    gym = models.ForeignKey(Gym, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self) -> str:
        return self.turno
    
class Plan(models.Model):
    plan = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.plan
    
class Entrenamiento(models.Model):
    entrenamiento = models.CharField(max_length=100)
    descripcion = models.TextField(default='Ingrese descripción')

    def __str__(self) -> str:
        return self.entrenamiento
    
class Rutina(models.Model):
    plan = models.ForeignKey(Plan, on_delete=models.SET_NULL, null=True, blank=True)
    rutina = models.CharField(max_length=100, default='', blank=True)
    repeticiones = models.IntegerField()
    series = models.IntegerField()
    
    def __str__(self) -> str:
        return f"{self.rutina} - {self.repeticiones} - {self.series}"
    
class GymbroporTurno(models.Model):
    turno = models.ForeignKey(Turno, on_delete=models.CASCADE)
    gymbro = models.ForeignKey(Gymbro, on_delete=models.CASCADE)
    entrenamiento = models.ForeignKey(Entrenamiento, on_delete=models.CASCADE, default=None, blank=True, null=True)
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE, default=None, blank=True, null=True)

    def __str__(self) -> str:
        return f"{self.gymbro} - {self.turno}: {self.entrenamiento} - {self.plan}"
