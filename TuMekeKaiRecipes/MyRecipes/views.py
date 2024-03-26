from django.shortcuts import render, HttpResponse, redirect
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy

from .models import Recipe
from . import models


recipes = [
    {
        "title" : "Chocolate Brownie", 
        "author" : " Jono Clarke",
        "description" : "Literally throw all your ingredients into a bowl, mix well, and bake until nice and gooey in the middle",
        "date_published" : "22nd July 2023"
    },
    {
        "title" : "Grilled Venision w' Red Wine Jus", 
        "author" : " Brandine Meyers",
        "description" : "Free Range Vensions served on a bed of Creamy Garlic Mash with homemade Red Wine Jus",
        "date_published" : "29th February 2020"
    },
    {
        "title" : "Chai Sui Pork", 
        "author" : "Helen Zhang",
        "description" : "   ",
        "date_published" : "25th December 2011"
    }
]
# Create your views here.

# ========= base page rendering =========
def base(request):
    return render(request, 'MyRecipes/base.html')


# ========= index page rendering =========
def index(request):
    context = {
        'recipes' : recipes
    }
    return render(request, 'MyRecipes/index.html', context)


class RecipeListView(ListView):
    model = models.Recipe
    template_name = 'recipes/recipe.html'
    context_object_name = 'recipes'


class RecipeDetailView(DetailView):
    model = models.Recipe


class RecipeCreateView(LoginRequiredMixin, CreateView):
    model = models.Recipe
    fields = ['title', 'description', 'category', 'subcategory', 'tags', 'ingredients', 'instructions']

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.save()
        return super().form_valid(form)
    


class RecipeUpdateView(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
    model = models.Recipe
    fields = ['title', 'description', 'category', 'subcategory', 'tags', 'ingredients', 'instructions']


    # checking if before recipe is modified, that it is the same author who created it
    def test_func(self):
        recipe = self.get_object()
        return self.request.user == recipe.author


    


class RecipeDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = models.Recipe
    success_url = reverse_lazy('recipes-home')


    # checking if before recipe is modified, that it is the same author who created it
    def test_func(self):
        recipe = self.get_object()
        return self.request.user == recipe.author


    def form_valid(self, form):
        form.instance.author = self.request.user
        form.save()
        return super().form_valid(form)
    
    


# ========= recipe page rendering =========
def recipes(request):
    recipes = models.Recipe.objects.all()
    context = {
        'recipes' : recipes
    }
    return render(request, 'MyRecipes/recipes.html', context)


# ========= catergory page rendering =========
def breakfast_recipes(request):
    recipes = Recipe.objects.filter(category='breakfast') 
    return render(request, 'MyRecipes/recipe_list.html', {'recipes': recipes})


def lunch_recipes(request):
    recipes = Recipe.objects.filter(category='lunch') 
    return render(request, 'MyRecipes/recipe_list.html', {'recipes': recipes})


def dinner_recipes(request):
    recipes = Recipe.objects.filter(category='dinner') 
    return render(request, 'MyRecipes/recipe_list.html', {'recipes': recipes})


def dessert_recipes(request):
    recipes = Recipe.objects.filter(category='dessert') 
    return render(request, 'MyRecipes/recipe_list.html', {'recipes': recipes})


def drinks_recipes(request):
    recipes = Recipe.objects.filter(category='drinks') 
    return render(request, 'MyRecipes/recipe_list.html', {'recipes': recipes})


def platter_recipes(request):
    recipes = Recipe.objects.filter(category='platter') 
    return render(request, 'MyRecipes/recipe_list.html', {'recipes': recipes})

def healthy_recipes(request):
    recipes = Recipe.objects.filter(category='healthy') 
    return render(request, 'MyRecipes/recipe_list.html', {'recipes': recipes})

def keto_recipes(request):
    recipes = Recipe.objects.filter(category='keto') 
    return render(request, 'MyRecipes/recipe_list.html', {'recipes': recipes})

def vegetarian_recipes(request):
    recipes = Recipe.objects.filter(category='vegetarian') 
    return render(request, 'MyRecipes/recipe_list.html', {'recipes': recipes})

def mothersDay_recipes(request):
    recipes = Recipe.objects.filter(category='mothers_day') 
    return render(request, 'MyRecipes/recipe_list.html', {'recipes': recipes})

def NewYears_recipes(request):
    recipes = Recipe.objects.filter(category='new_years') 
    return render(request, 'MyRecipes/recipe_list.html', {'recipes': recipes})







# ============== list with search =============
def recipe_list(request):
    query = request.GET.get('search')
    if query:
        query_lower = query.lower()
        recipes = Recipe.objects.filter(category__icontains = query_lower)
    else:
        recipes = Recipe.objects.all()
    return render(request, 'MyRecipes/recipe_list.html', {'recipes': recipes})



# def add(request):
#     if request.method == 'POST':
#         title = request.POST.get('title')
#         ingredients = request.POST.get('ingredients')
#         instructions = request.POST.get('instructions')
#         tags = request.POST.getlist('tags')  # Get list of selected tag IDs
        
#         recipe = Recipe.objects.create(
#             title=title,
#             ingredients=ingredients,
#             instructions=instructions
#         )
#         recipe.tags.add(*tags)  # Associate selected tags with the recipe
        
#         return redirect('recipe_list')  # Redirect to recipe list page
    
#     # Render the form
#     return render(request, 'MyRecipes/add_recipes.html', {'tags': Tag.objects.all()})



# def create_recipe(request):
#     if request.method == 'POST':
#         # Get form data
#         title = request.POST.get('title')
#         description = request.POST.get('description')
#         category = request.POST.get('category')
#         subcategory = request.POST.get('subcategory')
#         # Assuming 'tags' is a comma-separated string of tag names
#         tags_str = request.POST.get('tags')
#         tags = [tag.strip() for tag in tags_str.split(',')]

#         # Create and save recipe object
#         recipe = Recipe.objects.create(
#             title=title,
#             description=description,
#             category=category,
#             subcategory=subcategory,
#             author=request.user  # Assuming you're using Django's authentication system
#         )
        
#         # Set tags for the recipe
#         recipe.tags.clear()  # Clear existing tags
#         for tag_name in tags:
#             tag, _ = Tag.objects.get_or_create(name=tag_name)
#             recipe.tags.add(tag)

#         return redirect('r', recipe_id=recipe.id)  # Redirect to the detail view of the created recipe

#     return render(request, '/MyRecipes/create_recipe.html')  # Render the create recipe page


