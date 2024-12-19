from django.db import models

class ObjetConnecte(models.Model):
    TYPE_CHOICES = [
        ('CAPTEUR', 'Capteur'),
        ('ACTIONNEUR', 'Actionneur'),
        ('AUTRE', 'Autre'),
    ]
    
    ETAT_CHOICES = [
        ('ACTIF', 'Actif'),
        ('INACTIF', 'Inactif'),
        ('MAINTENANCE', 'En maintenance'),
    ]
    
    nom = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    type_objet = models.CharField(max_length=20, choices=TYPE_CHOICES, default='AUTRE')
    etat = models.CharField(max_length=20, choices=ETAT_CHOICES, default='INACTIF')
    date_installation = models.DateField()
    derniere_maintenance = models.DateField(null=True, blank=True)
    localisation = models.CharField(max_length=200)
    
    def __str__(self):
        return f"{self.nom} ({self.get_type_objet_display()})" 