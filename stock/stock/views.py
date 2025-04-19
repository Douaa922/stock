from django.shortcuts import render, redirect, get_object_or_404
from .models import Client, Fournisseur, Categorie, Produit, MouvementStock
from .forms import ClientForm, FournisseurForm, CategorieForm, ProduitForm
from django.db.models import Sum, Q
from .models import MouvementStock
from .forms import MouvementStockForm


# ----------------- MOUVEMENTS DE STOCK -----------------
def ajouter_mouvement(request):
    form = MouvementStockForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('liste_mouvements')
    return render(request, 'stock/ajouter_mouvement.html', {'form': form})

def liste_mouvements(request):
    query = request.GET.get('q')
    if query:
        mouvements = MouvementStock.objects.filter(
            Q(produit__nom__icontains=query) |
            Q(type_mouvement__icontains=query) |
            Q(client__nom__icontains=query) |
            Q(fournisseur__nom__icontains=query)
        )
    else:
        mouvements = MouvementStock.objects.all().order_by('-date_mouvement')
    return render(request, 'stock/liste_mouvements.html', {'mouvements': mouvements, 'query': query})

# ----------------- PRODUITS -----------------
def ajouter_produit(request):
    form = ProduitForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('liste_produits')
    return render(request, 'stock/ajouter_produit.html', {'form': form})

def liste_produits(request):
    query = request.GET.get('q')
    if query:
        produits = Produit.objects.filter(
            Q(nom__icontains=query) |
            Q(description__icontains=query) |
            Q(categorie__nom__icontains=query) |
            Q(fournisseur__nom__icontains=query)
        )
    else:
        produits = Produit.objects.all()
    return render(request, 'stock/liste_produits.html', {'produits': produits, 'query': query})

def modifier_produit(request, id):
    produit = get_object_or_404(Produit, id=id)
    form = ProduitForm(request.POST or None, instance=produit)
    if form.is_valid():
        form.save()
        return redirect('liste_produits')
    return render(request, 'stock/modifier_produits.html', {'form': form})

def supprimer_produit(request, id):
    produit = get_object_or_404(Produit, id=id)
    if request.method == 'POST':
        produit.delete()
        return redirect('liste_produits')
    return render(request, 'stock/supprimer_produit.html', {'produit': produit})

# ----------------- CLIENTS -----------------
def ajouter_client(request):
    form = ClientForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('liste_clients')
    return render(request, 'stock/ajouter_client.html', {'form': form})

def liste_clients(request):
    query = request.GET.get('q')
    if query:
        clients = Client.objects.filter(
            Q(nom__icontains=query) |
            Q(email__icontains=query) |
            Q(telephone__icontains=query)
        )
    else:
        clients = Client.objects.all()
    return render(request, 'stock/liste_clients.html', {'clients': clients, 'query': query})

def modifier_client(request, id):
    client = get_object_or_404(Client, id=id)
    form = ClientForm(request.POST or None, instance=client)
    if form.is_valid():
        form.save()
        return redirect('liste_clients')
    return render(request, 'stock/modifier_client.html', {'form': form})

def supprimer_client(request, id):
    client = get_object_or_404(Client, id=id)
    if request.method == 'POST':
        client.delete()
        return redirect('liste_clients')
    return render(request, 'stock/supprimer_client.html', {'client': client})

# ----------------- FOURNISSEURS -----------------
def ajouter_fournisseur(request):
    form = FournisseurForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('liste_fournisseurs')
    return render(request, 'stock/ajouter_fournisseur.html', {'form': form})

def liste_fournisseurs(request):
    query = request.GET.get('q')
    if query:
        fournisseurs = Fournisseur.objects.filter(
            Q(nom__icontains=query) |
            Q(email__icontains=query) |
            Q(telephone__icontains=query) |
            Q(pays__icontains=query) |
            Q(gouvernorat__icontains=query)
        )
    else:
        fournisseurs = Fournisseur.objects.all()
    return render(request, 'stock/liste_fournisseurs.html', {'fournisseurs': fournisseurs, 'query': query})

def modifier_fournisseurs(request, id):
    fournisseur = get_object_or_404(Fournisseur, id=id)
    form = FournisseurForm(request.POST or None, instance=fournisseur)
    if form.is_valid():
        form.save()
        return redirect('liste_fournisseurs')
    return render(request, 'stock/modifier_fournisseurs.html', {'form': form})

def supprimer_fournisseurs(request, id):
    fournisseur = get_object_or_404(Fournisseur, id=id)
    if request.method == 'POST':
        fournisseur.delete()
        return redirect('liste_fournisseurs')
    return render(request, 'stock/supprimer_fournisseurs.html', {'fournisseur': fournisseur})

# ----------------- CATÉGORIES -----------------
def ajouter_categorie(request):
    form = CategorieForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('liste_categories')
    return render(request, 'stock/ajouter_categorie.html', {'form': form})

def liste_categories(request):
    query = request.GET.get('q')
    if query:
        categories = Categorie.objects.filter(
            Q(nom__icontains=query)
        )
    else:
        categories = Categorie.objects.all()
    return render(request, 'stock/liste_categories.html', {'categories': categories, 'query': query})

def modifier_categories(request, id):
    categorie = get_object_or_404(Categorie, id=id)
    form = CategorieForm(request.POST or None, instance=categorie)
    if form.is_valid():
        form.save()
        return redirect('liste_categories')
    return render(request, 'stock/modifier_categories.html', {'form': form})

def supprimer_categories(request, id):
    categorie = get_object_or_404(Categorie, id=id)
    if request.method == 'POST':
        categorie.delete()
        return redirect('liste_categories')
    return render(request, 'stock/supprimer_categories.html', {'categorie': categorie})

# ----------------- DASHBOARD -----------------
#def dashboard(request):
    total_produits = Produit.objects.count()
    total_clients = Client.objects.count()
    total_fournisseurs = Fournisseur.objects.count()
    total_entrees = MouvementStock.objects.filter(type_mouvement='ENTREE').aggregate(Sum('quantite'))['quantite__sum'] or 0
    total_sorties = MouvementStock.objects.filter(type_mouvement='SORTIE').aggregate(Sum('quantite'))['quantite__sum'] or 0
    return render(request, 'stock/dashboard.html', {
        'total_produits': total_produits,
        'total_clients': total_clients,
        'total_fournisseurs': total_fournisseurs,
        'total_entrees': total_entrees,
        'total_sorties': total_sorties,
    })

def dashboard_mouvements(request):
    total_mouvements = MouvementStock.objects.count()
    total_entrees = MouvementStock.objects.filter(type_mouvement='ENTREE').aggregate(Sum('quantite'))['quantite__sum'] or 0
    total_sorties = MouvementStock.objects.filter(type_mouvement='SORTIE').aggregate(Sum('quantite'))['quantite__sum'] or 0

    derniers_mouvements = MouvementStock.objects.order_by('-date_mouvement')[:5]

    produits_plus_sortis = (
        MouvementStock.objects
        .filter(type_mouvement='SORTIE')
        .values('produit__nom')
        .annotate(total_sortie=Sum('quantite'))
        .order_by('-total_sortie')[:5]
    )

    return render(request, 'stock/dashboard.html', {
        'total_mouvements': total_mouvements,
        'total_entrees': total_entrees,
        'total_sorties': total_sorties,
        'derniers_mouvements': derniers_mouvements,
        'produits_plus_sortis': produits_plus_sortis,
    })

