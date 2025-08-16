import ast
import os
import csv
from datetime import datetime

from recipe.domainmodel.author import Author
from recipe.domainmodel.category import Category
from recipe.domainmodel.nutrition import Nutrition
from recipe.domainmodel.recipe import Recipe

class CSVDataReader:
    def __init__(self):
        self.csv_file = os.path.join(os.path.dirname(__file__), '..', 'data', 'recipes.csv')
        self.authors = []
        self.categories = []
        self.recipes = []
        self._read_csv()

    def _read_csv(self):
        if not os.path.exists(self.csv_file):
            raise FileNotFoundError(f"CSV file not found: {self.csv_file}")

        author_dict = {}
        category_dict = {}
        category_id_counter = 1

        with open(self.csv_file, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                recipe_id = int(row['RecipeId'])
                name = row['Name']
                author_id = int(row['AuthorId'])
                author_name = row['AuthorName']
                cook_time = int(row['CookTime']) if row['CookTime'] and row['CookTime'] != 'NA' else 0
                prep_time = int(row['PrepTime']) if row['PrepTime'] and row['PrepTime'] != 'NA' else 0
                date_published = self._parse_date(row['DatePublished'])
                description = row['Description']
                images_str = row['Images']
                images = ast.literal_eval(images_str) if images_str and images_str != 'NA' else []
                category_name = row['RecipeCategory']
                ingredient_quantities_str = row['RecipeIngredientQuantities']
                ingredient_quantities = ast.literal_eval(ingredient_quantities_str) if ingredient_quantities_str and ingredient_quantities_str != 'NA' else []
                ingredient_parts_str = row['RecipeIngredientParts']
                ingredients = ast.literal_eval(ingredient_parts_str) if ingredient_parts_str and ingredient_parts_str != 'NA' else []
                nutrition = Nutrition()
                nutrition.calories = float(row['Calories']) if row['Calories'] and row['Calories'] != 'NA' else None
                nutrition.fat_content = float(row['FatContent']) if row['FatContent'] and row['FatContent'] != 'NA' else None
                nutrition.saturated_fat_content = float(row['SaturatedFatContent']) if row['SaturatedFatContent'] and row['SaturatedFatContent'] != 'NA' else None
                nutrition.cholesterol_content = float(row['CholesterolContent']) if row['CholesterolContent'] and row['CholesterolContent'] != 'NA' else None
                nutrition.sodium_content = float(row['SodiumContent']) if row['SodiumContent'] and row['SodiumContent'] != 'NA' else None
                nutrition.carbohydrate_content = float(row['CarbohydrateContent']) if row['CarbohydrateContent'] and row['CarbohydrateContent'] != 'NA' else None
                nutrition.fiber_content = float(row['FiberContent']) if row['FiberContent'] and row['FiberContent'] != 'NA' else None
                nutrition.sugar_content = float(row['SugarContent']) if row['SugarContent'] and row['SugarContent'] != 'NA' else None
                nutrition.protein_content = float(row['ProteinContent']) if row['ProteinContent'] and row['ProteinContent'] != 'NA' else None
                servings = row['RecipeServings'] if row['RecipeServings'] != 'NA' else None
                recipe_yield = row['RecipeYield'] if row['RecipeYield'] != 'NA' else None
                instructions_str = row['RecipeInstructions']
                instructions = ast.literal_eval(instructions_str) if instructions_str and instructions_str != 'NA' else []

                if author_id not in author_dict:
                    author = Author(author_id, author_name)
                    author_dict[author_id] = author
                    self.authors.append(author)
                else:
                    author = author_dict[author_id]

                if category_name not in category_dict:
                    category = Category(name=category_name, category_id=category_id_counter)
                    category_dict[category_name] = category
                    self.categories.append(category)
                    category_id_counter += 1
                else:
                    category = category_dict[category_name]

                recipe = Recipe(
                    recipe_id=recipe_id,
                    name=name,
                    author=author,
                    cook_time=cook_time,
                    preparation_time=prep_time,
                    created_date=date_published,
                    description=description,
                    images=images,
                    category=category,
                    ingredient_quantities=ingredient_quantities,
                    ingredients=ingredients,
                    nutrition=nutrition,
                    servings=servings,
                    recipe_yield=recipe_yield,
                    instructions=instructions
                )

                self.recipes.append(recipe)
                author.add_recipe(recipe)
                category.add_recipe(recipe)

    def _parse_date(self, date_str: str) -> datetime:
        if not date_str:
            return None
        date_str = date_str.replace('st ', ' ').replace('nd ', ' ').replace('rd ', ' ').replace('th ', ' ')
        try:
            return datetime.strptime(date_str, '%d %b %Y')
        except ValueError:
            try:
                return datetime.strptime(date_str, '%Y-%m-%d')
            except ValueError:
                return None