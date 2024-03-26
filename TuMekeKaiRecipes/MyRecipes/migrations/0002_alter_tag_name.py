# Generated by Django 5.0.3 on 2024-03-22 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyRecipes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(choices=[('breakfast', 'Breakfast'), ('lunch', 'Lunch'), ('dinner', 'Dinner'), ('dessert', 'Dessert'), ('drinks', 'Drinks'), ('platter', 'Platter'), ('other', 'Other'), ('holiday_specials', 'Holiday Specials'), ('healthy_choices', 'Healthy Choices'), ('quick_and_easy', 'Quick & Easy'), ('budget_friendly', 'Budget-friendly'), ('comfort_food', 'Comfort Food'), ('international_cuisine', 'International Cuisine'), ('baking', 'Baking'), ('grilling_and_bbq', 'Grilling & BBQ'), ('vegetarian_vegan', 'Vegetarian/Vegan'), ('gluten_free', 'Gluten-Free'), ('dairy_free', 'Dairy-Free'), ('low_carb', 'Low Carb'), ('high_protein', 'High Protein'), ('keto', 'Keto'), ('paleo', 'Paleo'), ('whole30', 'Whole30'), ('mediterranean', 'Mediterranean'), ('asian_inspired', 'Asian-Inspired'), ('mexican', 'Mexican'), ('italian', 'Italian'), ('middle_eastern', 'Middle Eastern')], max_length=50),
        ),
    ]
