from django.contrib.auth.views import LoginView
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login as django_login
from .forms import CustomAuthenticationForm, CustomUserCreationForm

from . import models
from . import forms

def index(request):
    return render (request, "gym_admin/index.html")

class CustomLoginView(LoginView):
    authentication_form = CustomAuthenticationForm
    template_name = "gym_admin/login.html"
    
def register(request):
    print("dentro de la funcion register")
    if request.method == "POST":
        print("dentro de POST")
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            print("dentro de is_valid")
            form.save()
            return redirect("index")
    else:  # if request.method == "GET":
        form = CustomUserCreationForm()
    return render(request, "gym_admin/index.html", {"form": form})

def gym_admin(request):
    return render (request, "gym_admin/gym_admin.html")

def gym_list(request):
    consulta = models.Gym.objects.all()
    contexto = {"Gimnasios": consulta}
    return render(request, "gym_admin/gym_list.html", contexto)

def gym_form(request):
    if request.method == "POST":
        form = forms.GymForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("gym_list")
    else:
        form = forms.GymForm()
    return render (request, "gym_admin/gym_form.html", {"form": form})

def gymbro_list(request):
    consulta = models.Gymbro.objects.all()
    contexto = {"Gymbros": consulta}
    return render(request, "gym_admin/gymbro_list.html", contexto)

def gymbro_form(request):
    if request.method == "POST":
        form = forms.GymbroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("gymbro_list")
    else:
        form = forms.GymbroForm()
    return render (request, "gym_admin/gymbro_form.html", {"form": form})

def turno_list(request):
    consulta = models.Turno.objects.all()
    contexto = {"Turnos": consulta}
    return render(request, "gym_admin/turno_list.html", contexto)

def turno_form(request):
    if request.method == "POST":
        form = forms.TurnoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("turno_list")
    else:
        form = forms.TurnoForm()
    return render (request, "gym_admin/turno_form.html", {"form": form})

def entrenamiento_list(request):
    consulta = models.Entrenamiento.objects.all()
    contexto = {"Entrenamientos": consulta}
    return render(request, "gym_admin/entrenamiento_list.html", contexto)

def entrenamiento_form(request):
    if request.method == "POST":
        form = forms.EntrenamientoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("entrenamiento_list")
    else:
        form = forms.EntrenamientoForm()
    return render (request, "gym_admin/entrenamiento_form.html", {"form": form})

def plan_list(request):
    consulta = models.Plan.objects.all()
    contexto = {"Planes": consulta}
    return render(request, "gym_admin/plan_list.html", contexto)

def plan_form(request):
    if request.method == "POST":
        form = forms.PlanForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("plan_list")
    else:
        form = forms.PlanForm()
    return render (request, "gym_admin/plan_form.html", {"form": form})

def rutina_list(request):
    consulta = models.Rutina.objects.all()
    contexto = {"Rutinas": consulta}
    return render(request, "gym_admin/rutina_list.html", contexto)

def rutina_form(request):
    if request.method == "POST":
        form = forms.RutinaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("rutina_list")
    else:
        form = forms.RutinaForm()
    return render (request, "gym_admin/rutina_form.html", {"form": form})

def plangymbro_list(request):
    consulta = models.GymbroporTurno.objects.all()
    contexto = {"PlanesGymBro": consulta}
    return render(request, "gym_admin/plangymbro_list.html", contexto)

def plangymbro_form(request):
    if request.method == "POST":
        form = forms.PlangymbroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("plangymbro_list")
    else:
        form = forms.PlangymbroForm()
    return render (request, "gym_admin/plangymbro_form.html", {"form": form})

