from django.urls import path
from . import views

app_name = 'objets'

urlpatterns = [
    path('', views.liste_objets, name='liste_objets'),
    path('ajouter/', views.ajouter_objet, name='ajouter_objet'),
    path('edit/<int:pk>/', views.edit_objet, name='edit_objet'),
    path('delete/<int:pk>/', views.delete_objet, name='delete_objet'),
] 