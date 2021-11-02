from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='title_search'),
    path('search_ingridient', views.index2, name='ingredient_search'),
    path('recipes/<int:recipe_id>', views.get_recipe, name='recipes'),
]
