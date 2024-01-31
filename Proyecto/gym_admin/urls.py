from django.contrib.auth.views import LogoutView
from django.urls import path

from .views import *
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path("login/", CustomLoginView.as_view(), name="login"),
    path('gym_admin', views.gym_admin, name="gym_admin"),
    path('gym/list', views.gym_list, name="gym_list"),
    path('gym/form', views.gym_form, name="gym_form"),
    path('gymbro/list', views.gymbro_list, name="gymbro_list"),
    path('gymbro/form', views.gymbro_form, name="gymbro_form"),
    path('turno/list', views.turno_list, name="turno_list"),
    path('turno/form', views.turno_form, name="turno_form"),
    path('entrenamiento/list', views.entrenamiento_list, name="entrenamiento_list"),
    path('entrenamiento/form', views.entrenamiento_form, name="entrenamiento_form"),
    path('plan/list', views.plan_list, name="plan_list"),
    path('plan/form', views.plan_form, name="plan_form"),
    path('rutina/list', views.rutina_list, name="rutina_list"),
    path('rutina/form', views.rutina_form, name="rutina_form"),
    path('plangymbro/list', views.plangymbro_list, name="plangymbro_list"),
    path('plangymbro/form', views.plangymbro_form, name="plangymbro_form"),
    path("logout/", LogoutView.as_view(template_name="gym_admin/logout.html"), name="logout"),
    path("register/", views.register, name="register"),
]
