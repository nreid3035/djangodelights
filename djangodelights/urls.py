"""djangodelights URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from inventory import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.landing, name='landing'),
    path('home/', views.home, name='home'),
    path('account/', views.account, name='account'),
    path('ingredient-list/', views.IngredientListView.as_view(), name='ingredientlist'),
    path('ingredient/create', views.IngredientCreateView.as_view(), name='ingredientcreate'),
    path('ingredient/<pk>', views.IngredientView.as_view(), name='ingredient'),
    path('menu-list/', views.MenuListView.as_view(), name='menulist'),
    path('menu/create', views.MenuCreateView.as_view(), name='menucreate'),
    path('menu/<pk>', views.MenuView.as_view(), name='menuitem'),
    path('purchase-list/', views.PurchaseListView.as_view(), name='purchaselist'),
    path('purchase/create', views.PurchaseCreateView.as_view(), name='purchasecreate'),
    path('purchase/<pk>', views.PurchaseView.as_view(), name='purchase'),
    path('recipe/create', views.RecipeCreateView.as_view(), name='recipecreate'),
    path('recipe/<pk>', views.RecipeView.as_view(), name='recipe')
    
]
