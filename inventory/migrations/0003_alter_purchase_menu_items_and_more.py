# Generated by Django 4.1 on 2022-09-03 01:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_alter_menuitem_menu_price_alter_menuitem_recipe'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='menu_items',
            field=models.JSONField(default={}),
        ),
        migrations.AlterField(
            model_name='reciperequirement',
            name='ingredient_list',
            field=models.JSONField(default={}),
        ),
    ]
