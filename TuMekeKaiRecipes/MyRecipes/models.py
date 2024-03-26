from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
import os


# Create your models here. --> model is a table in the database
# Django --> ORM "Object Relation Method"

class Tag(models.Model):
    TAG_CHOICES = [
        ('breakfast', 'Breakfast'),
        ('lunch', 'Lunch'),
        ('dinner', 'Dinner'),
        ('dessert', 'Dessert'),
        ('drinks', 'Drinks'),
        ('platter', 'Platter'),
        ('other', 'Other'),
        ('holiday_specials', 'Holiday Specials'),
        ('healthy_choices', 'Healthy Choices'),
        ('healthy', 'Healthy '),
        ('quick_and_easy', 'Quick & Easy'),
        ('budget_friendly', 'Budget-friendly'),
        ('comfort_food', 'Comfort Food'),
        ('international_cuisine', 'International Cuisine'),
        ('baking', 'Baking'),
        ('grilling_and_bbq', 'Grilling & BBQ'),
        ('vegetarian_vegan', 'Vegetarian/Vegan'),
        ('gluten_free', 'Gluten-Free'),
        ('dairy_free', 'Dairy-Free'),
        ('low_carb', 'Low Carb'),
        ('high_protein', 'High Protein'),
        ('keto', 'Keto'),
        ('paleo', 'Paleo'),
        ('whole30', 'Whole30'),
        ('mediterranean', 'Mediterranean'),
        ('asian_inspired', 'Asian-Inspired'),
        ('mexican', 'Mexican'),
        ('italian', 'Italian'),
        ('middle_eastern', 'Middle Eastern'),
    ]


    name = models.CharField(max_length = 50, choices = TAG_CHOICES)

    def __str__(self):
        return self.name




class Recipe(models.Model):
    CATEGORY_CHOICES = [
        ('breakfast', 'Breakfast'),
        ('lunch', 'Lunch'),
        ('dinner', 'Dinner'),
        ('dessert', 'Dessert'),
        ('drinks', 'Drinks'),
        ('platter', 'Platter'),
        ('other', 'Other'),
        ('holiday_specials', 'Holiday Specials'),
        ('healthy_choices', 'Healthy Choices'),
        ('healthy', 'Healthy'),
        ('budget_friendly', 'Budget-friendly'),
        ('comfort_food', 'Comfort Food'),
        ('international_cuisine', 'International Cuisine'),
        ('baking', 'Baking'),
        ('grilling_and_bbq', 'Grilling & BBQ'),
        ('vegetarian_vegan', 'Vegetarian/Vegan'),
        ('vegetarian', 'Vegetarian'),
        ('gluten_free', 'Gluten-Free'),
        ('dairy_free', 'Dairy-Free'),
        ('low_carb', 'Low Carb'),
        ('high_protein', 'High Protein'),
        ('keto', 'Keto'),
        ('paleo', 'Paleo'),
        ('whole30', 'Whole30'),
        ('mediterranean', 'Mediterranean'),
        ('asian_inspired', 'Asian-Inspired'),
        ('mexican', 'Mexican'),
        ('italian', 'Italian'),
        ('middle_eastern', 'Middle Eastern'),
        ('new_years', 'New Years'),
        ('mothers_day', 'Mothers Day'),
    ]

    SUBCATEGORY_CHOICES = [
        ('vegetarian', 'Vegetarian'),
        ('vegan', 'Vegan'),
        ('gluten_free', 'Gluten free'),
        ('low_carb', 'Low Carb'),
        ('high_protein', 'High Protein'),
        ('keto', 'Keto'),
        ('other', 'Other'),
        ('paleo', 'Paleo-Friendly'),
        ('whole30', 'Whole30-Compliant'),
        ('mediterranean', 'Mediterranean Diet'),
        ('weight_loss', 'Weight Loss'),
        ('heart_healthy', 'Heart-Healthy'),
        ('diabetes_friendly', 'Diabetes-Friendly'),
        ('nut_free', 'Nut-Free'),
        ('soy_free', 'Soy-Free'),
        ('nutrient_dense', 'Nutrient-Dense'),
        ('light_and_fresh', 'Light & Fresh'),
        ('family_friendly', 'Family-Friendly'),
        ('kid_friendly', 'Kid-Friendly'),
        ('party_appetizers', 'Party Appetizers'),
        ('seasonal_produce', 'Seasonal Produce'),
        ('one_pot_meals', 'One-Pot Meals'),
        ('meal_prep', 'Meal Prep'),
        ('slow_cooker', 'Slow Cooker/Crockpot'),
        ('instant_pot', 'Instant Pot/Pressure Cooker'),
        ('raw_foods', 'Raw Foods'),
        ('superfoods', 'Superfoods'),
        ('detoxifying', 'Detoxifying'),
        ('immune_boosting', 'Immune-Boosting'),
        ('energy_packed', 'Energy-Packed'),
    ]


    # assigning datatypes to appropriate fields/attributes
    title = models.CharField(max_length = 100)
    description = models.TextField()

    author = models.ForeignKey(User, on_delete = models.CASCADE) # is user deleted -- delete recipxes user put up --> FK = 1 (user) - N(recipes)

    category = models.CharField(max_length = 25, choices = CATEGORY_CHOICES, default = "other")
    subcategory = models.CharField(max_length = 25, choices = SUBCATEGORY_CHOICES, default = "other")

    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    tags = models.ManyToManyField(Tag) 
    
    image = models.ImageField(upload_to='Images/', blank=True)

    ingredients = models.TextField(blank=True, null=True)
    instructions = models.TextField(blank=True, null=True)

    def get_absolute_url(self):
        return reverse("recipes-detail", kwargs = {"pk": self.pk})
    

    def __str__(self):
        return self.title
    
    def filename(self):
        return os.path.basename(self.image.name)
    



