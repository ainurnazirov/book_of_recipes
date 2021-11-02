from django.shortcuts import render
from .models import Recipe, Ingredient
from django.shortcuts import get_object_or_404


def index(request):
    recipes = Recipe.objects.all()

    return render(request, 'index.html', {'recipes': recipes})


def search(request, search_type):
    if request.method == "POST":
        if search_type == 0 and request.POST.get("search") != '':
            query = request.POST.get("search")
            recipes = Recipe.objects.filter(title_recipe__contains=query)
        elif search_type == 1 and request.POST.get("search2") != '':
            query = request.POST.get("search2").lower()
            if Ingredient.objects.filter(title_ingredient__contains=query).exists():
                ingredient_id = Ingredient.objects.filter(title_ingredient__contains=query)[0].id
                recipes = Recipe.objects.filter(ingredients=ingredient_id)
            else:
                recipes = Recipe.objects.none()
        else:
            recipes = Recipe.objects.none()
    else:
        recipes = Recipe.objects.none()

    return render(request, 'index.html', {'recipes': recipes})


def get_recipe(request, recipe_id):
    recipe_item = get_object_or_404(Recipe, pk=recipe_id)

    return render(request, 'recipe.html', {'recipe': recipe_item})
