# Generated by Django 3.2.8 on 2021-10-31 19:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipesapp', '0003_recipe_ingredient'),
    ]

    operations = [
        migrations.DeleteModel(
            name='RecipeIngredient',
        ),
    ]
