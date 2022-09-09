from django.views.generic import ListView, DetailView
from django.shortcuts import render

from inventory.models import Ingredient, MenuItem, Purchase, RecipeRequirement

# Create your views here.
def landing(request):
    return render(request, 'inventory/landing.html')

def home(request):
    return render(request, 'inventory/home.html')

#def recipe(request):
#    return render(request, 'inventory/recipe.html')

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

class RecipeView(DetailView):
    model = RecipeRequirement
    template_name = 'inventory/recipe.html'
    context_object_name = 'recipe'