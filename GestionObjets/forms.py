from django import forms
from .models import ObjetConnecte

class ObjetConnecteForm(forms.ModelForm):
    class Meta:
        model = ObjetConnecte
        fields = ['nom', 'description', 'type_objet', 'etat', 'date_installation', 'localisation']
        widgets = {
            'nom': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nom de l\'objet'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Description de l\'objet'
            }),
            'type_objet': forms.Select(attrs={
                'class': 'form-select'
            }),
            'etat': forms.Select(attrs={
                'class': 'form-select'
            }),
            'date_installation': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'localisation': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Localisation de l\'objet'
            })
        } 