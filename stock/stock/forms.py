from django import forms
from .models import Client, Fournisseur, Categorie, Produit , MouvementStock


class MouvementStockForm(forms.ModelForm):
    class Meta:
        model = MouvementStock
        fields = ['produit', 'type_mouvement', 'quantite', 'client']
class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['nom', 'pays', 'gouvernorat', 'telephone', 'email']

class FournisseurForm(forms.ModelForm):
    class Meta:
        model = Fournisseur
        fields = ['nom', 'pays', 'gouvernorat', 'telephone', 'email']

class CategorieForm(forms.ModelForm):
    class Meta:
        model = Categorie
        fields = ['nom']

class ProduitForm(forms.ModelForm):
    class Meta:
        model = Produit
        fields = ['nom', 'description', 'quantite_stock', 'prix_achat', 'prix_vente' ,'categorie', 'fournisseur']
