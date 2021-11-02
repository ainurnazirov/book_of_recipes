from django.shortcuts import render
from .models import Recipe, Ingredient


def index(request):
    recipes = Recipe.objects.all()

    if request.method == "POST":
        recipes = Recipe.objects.filter(title_recipe__contains=request.POST.get("search"))

    return render(request, 'index.html', {'recipes': recipes})


def index2(request):
    if request.method == "POST":
        if Ingredient.objects.filter(title_ingredient=request.POST.get("search2")).exists():
            ingredient_id = Ingredient.objects.filter(title_ingredient=request.POST.get("search2"))[0].id
            recipes = Recipe.objects.filter(ingredients=ingredient_id)
        else:
            recipes = Recipe.objects.none()

    return render(request, 'index.html', {'recipes': recipes})
