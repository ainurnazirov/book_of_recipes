from django.db import models


class Ingredient(models.Model):
    title_ingredient = models.CharField("Название ингридиента", max_length=50, unique=True, null=False)

    def __str__(self):
        return self.title_ingredient


class Recipe(models.Model):
    title_recipe = models.CharField("Название рецепта", max_length=100, null=False)
    text_recipe = models.TextField("Текст рецепта", max_length=1000, null=False)
    ingredients = models.ManyToManyField('Ingredient', blank=True, related_name='recipes')

    def __str__(self):
        return self.title_recipe
