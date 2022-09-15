from django import forms

from .models import Ingredient, MenuItem, RecipeRequirement, Purchase

class IngredientCreateForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = ['name', 'available', 'unit', 'price_per_unit', 'quantity_per_purchase']
    
class MenuCreateForm(forms.ModelForm):
    class Meta:
        model = MenuItem
        fields = ['name', 'menu_price']
    
class RecipeCreateForm(forms.ModelForm):
    class Meta:
        model = RecipeRequirement
        fields = ['menu_item', 'ingredient_list']
    
class PurchaseCreateForm(forms.ModelForm):
    class Meta:
        model = Purchase
        fields = ['total_price', 'menu_items']
    