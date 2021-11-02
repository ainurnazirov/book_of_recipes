from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='main_page'),
    path('recipes/<int:recipe_id>', views.get_recipe, name='recipes'),
    path('search/<int:search_type>', views.search, name='search'),
]
