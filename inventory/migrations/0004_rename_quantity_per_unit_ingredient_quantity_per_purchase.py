# Generated by Django 4.1 on 2022-09-04 01:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0003_alter_purchase_menu_items_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ingredient',
            old_name='quantity_per_unit',
            new_name='quantity_per_purchase',
        ),
    ]