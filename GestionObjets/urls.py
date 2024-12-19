from django.urls import path
from . import views

app_name = 'objets'

urlpatterns = [
    path('', views.liste_objets, name='liste_objets'),
    path('ajouter/', views.ajouter_objet, name='ajouter_objet'),
] 