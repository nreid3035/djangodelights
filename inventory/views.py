from django.views.generic import ListView
from django.shortcuts import render

from inventory.models import Ingredient, MenuItem, Purchase

# Create your views here.
def landing(request):
    return render(request, 'inventory/landing.html')

def home(request):
    return render(request, 'inventory/home.html')

class IngredientListView(ListView):
    model = Ingredient
    template_name = 'inventory/ingredient-list.html'
    context_object_name = 'ingredient_list'

class MenuListView(ListView):
    model = MenuItem
    template_name = 'inventory/menu-list.html'
    context_object_name = 'menu_list'

class PurchaseListView(ListView):
    model = Purchase
    template_name = 'inventory/purchase-list.html'
    context_object_name = 'purchase_list'