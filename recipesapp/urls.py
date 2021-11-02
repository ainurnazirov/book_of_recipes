from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'title_search'),
    path('search_ingridient', views.index2, name = 'ingredient_search'),
]
