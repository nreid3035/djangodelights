from tkinter import CASCADE
from django.db import models

# Create your models here.
class Ingredient(models.Model):
    name = models.CharField(max_length=30, primary_key=True)
    available = models.IntegerField(default=0)
    unit = models.CharField(max_length=20)
    price_per_unit = models.IntegerField(default=0)
    quantity_per_unit = models.IntegerField(default=0)

class MenuItem(models.Model):
    name = models.CharField(max_length=30, primary_key=True)
    recipe = models.IntegerField(default=None)
    menu_price = models.DecimalField(max_digits=5, decimal_places=2)

class RecipeRequirement(models.Model):
    def __init__(self, ingredients):  # Should I declare the initial properties like this or go the manager route in the django docs
        self.ingredients = ingredients
    menu_item = models.ForeignKey('MenuItem', on_delete=models.CASCADE)
    ingredient_list = models.JSONField() ####### Check back if self is being used properly !!! ########

class Purchase(models.Model):
    total_price = models.IntegerField(default=0)
    menu_items = models.JSONField()
    purchase_time = models.DateTimeField(auto_now=True)


