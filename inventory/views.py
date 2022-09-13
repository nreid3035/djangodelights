from django.views.generic import ListView, DetailView
from django.shortcuts import render

from inventory.models import Ingredient, MenuItem, Purchase, RecipeRequirement

# Create your views here.
# View for landing page
def landing(request):
    return render(request, 'inventory/landing.html')

# View for home page of a logged in user
def home(request):
    return render(request, 'inventory/home.html')

# View for account page of a user
def account(request):
    return render(request, 'inventory/account.html')


####### INGREDIENT CLASSES #########

# View for a list of ingredients
class IngredientListView(ListView):
    model = Ingredient
    template_name = 'inventory/ingredient-list.html'
    context_object_name = 'ingredient_list'

# View for an individual Ingredient by pk
class IngredientView(DetailView):
    model = Ingredient
    template_name = 'inventory/ingredient.html'
    context_object_name = 'ingredient'

####### MENUITEM CLASSES ########

# View for a list of Menu Items
class MenuListView(ListView):
    model = MenuItem
    template_name = 'inventory/menu-list.html'
    context_object_name = 'menu_list'

# View for a view of an individual menu item
class MenuView(DetailView):
    model = MenuItem
    template_name = 'inventory/menu.html'
    context_object_name = 'menu'

######## PURCHASE CLASSES #########
# View for a list of all purchases
class PurchaseListView(ListView):
    model = Purchase
    template_name = 'inventory/purchase-list.html'
    context_object_name = 'purchase_list'

# View for an individual purchase
class PurchaseView(DetailView):
    model = Purchase
    template_name = 'inventory/purchase.html'
    context_object_name = 'purchase'

######## RECIPEREQUIREMENTS CLASSES ########

# View for an individual Recipe by pk
class RecipeView(DetailView):
    model = RecipeRequirement
    template_name = 'inventory/recipe.html'
    context_object_name = 'recipe'