from django.urls import path
from . import views
from users import views as user_views


urlpatterns = [
    path('', views.index, name = 'recipes-home'),
    path('recipeL/', views.RecipeListView.as_view(), name = 'recipeL'),
    path('recipes/<int:pk>/', views.RecipeDetailView.as_view(), name = 'recipes-detail'),
    path('recipes/<int:pk>/update', views.RecipeUpdateView.as_view(), name = 'recipes-update'),
    path('recipes/<int:pk>/delete', views.RecipeDeleteView.as_view(), name = 'recipes-delete'),
    path('recipes/create/', views.RecipeCreateView.as_view(), name = 'recipes-create'),
    path('base/', views.base, name = 'recipes-base'),
    path('recipes/', views.recipes, name = "recipes-recipes"),
    path('recipes/breakfast/', views.breakfast_recipes, name='breakfast_recipes'),
    path('recipes/lunch/', views.lunch_recipes, name='lunch_recipes'),  
    path('recipes/dinner/', views.dinner_recipes, name='dinner_recipes'),  
    path('recipes/dessert/', views.dessert_recipes, name='dessert_recipes'),  
    path('recipes/drinks/', views.drinks_recipes, name='drinks_recipes'),  
    path('recipes/platter/', views.platter_recipes, name='platter_recipes'), 
    path('recipes/keto/', views.keto_recipes, name='recipes_keto'), 
    path('recipes/vegetarian/', views.vegetarian_recipes, name='recipes_vegetarian'), 
    path('recipes/healthy/', views.healthy_recipes, name='recipes_healthy'), 
    path('recipes/mothersDay/', views.mothersDay_recipes, name='recipes_mothersDay'), 
    path('recipes/NewYears/', views.NewYears_recipes, name='recipes_newYears'), 
    path('recipes/all/', views.recipe_list, name='recipe_all'),  # URL pattern for displaying all recipes :)
    
]
