from email.policy import default
from tkinter import CASCADE
from django.db import models

# Create your models here.
class Ingredient(models.Model):
    name = models.CharField(max_length=30, primary_key=True, unique=True)
    available = models.IntegerField(default=0)
    unit = models.CharField(max_length=20)
    price_per_unit = models.DecimalField(max_digits=5, decimal_places=2)
    quantity_per_purchase = models.DecimalField(max_digits=5, decimal_places=2)
    

class MenuItem(models.Model):
    name = models.CharField(max_length=30, primary_key=True, unique=True)
    menu_price = models.DecimalField(max_digits=5, decimal_places=2)

class RecipeRequirement(models.Model):
    menu_item = models.ForeignKey('MenuItem', on_delete=models.CASCADE, primary_key=True, unique=True)
    ingredient_list = models.JSONField(default=dict) 
    
class Purchase(models.Model):
    total_price = models.DecimalField(max_digits=5, decimal_places=2)
    menu_items = models.JSONField(default=dict) 
    purchase_time = models.DateTimeField(auto_now=True)


