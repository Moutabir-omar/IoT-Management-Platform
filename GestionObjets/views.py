from django.shortcuts import render, redirect
from django.contrib import messages
from .models import ObjetConnecte
from .forms import ObjetConnecteForm

def home(request):
    context = {
        'objets_recents': ObjetConnecte.objects.all().order_by('-date_installation')[:5],
        'objets_actifs': ObjetConnecte.objects.filter(etat='ACTIF'),
        'objets_inactifs': ObjetConnecte.objects.filter(etat='INACTIF'),
    }
    return render(request, 'home.html', context)

def liste_objets(request):
    objets = ObjetConnecte.objects.all()
    return render(request, 'objets/liste_objets.html', {'objets': objets})

def ajouter_objet(request):
    if request.method == 'POST':
        form = ObjetConnecteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Objet connecté ajouté avec succès!')
            return redirect('objets:liste_objets')
    else:
        form = ObjetConnecteForm()
    return render(request, 'objets/ajouter_objet.html', {'form': form}) 