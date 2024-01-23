from django import forms

from . import models

from django.contrib.auth.forms import AuthenticationForm

class CustomLoginForm(AuthenticationForm):
    # username = forms.CharField(label="Username", max_length=30)
    # password = forms.CharField(label="Password", max_length=30)
    pass    

class GymForm(forms.ModelForm):
    class Meta:
        model = models.Gym
        fields = "__all__"

class GymbroForm(forms.ModelForm):
    class Meta:
        model = models.Gymbro
        fields = "__all__"

class TurnoForm(forms.ModelForm):
    class Meta:
        model = models.Turno
        fields = "__all__"

class EntrenamientoForm(forms.ModelForm):
    class Meta:
        model = models.Entrenamiento
        fields = "__all__"

class PlanForm(forms.ModelForm):
    class Meta:
        model = models.Plan
        fields = "__all__"

class RutinaForm(forms.ModelForm):
    class Meta:
        model = models.Rutina
        fields = "__all__"

class PlangymbroForm(forms.ModelForm):
    class Meta:
        model = models.GymbroporTurno
        fields = "__all__"