import pytest
from datetime import datetime

from recipe.domainmodel.user import User
from recipe.domainmodel.author import Author
from recipe.domainmodel.category import Category
from recipe.domainmodel.recipe import Recipe
from recipe.domainmodel.nutrition import Nutrition
from recipe.domainmodel.favourite import Favourite
from recipe.domainmodel.review import Review

# Fixtures
@pytest.fixture
def my_user():
    return User("test_user", "password123", 1)

@pytest.fixture
def my_author():
    return Author(1, "Gordon Ramsay")

@pytest.fixture
def my_category():
    return Category("Italian", [], 1)

@pytest.fixture
def my_recipe(my_author, my_category):
    return Recipe(
        recipe_id=1,
        name="Spaghetti Carbonara",
        author=my_author,
        cook_time=20,
        preparation_time=15,
        created_date=datetime(2024, 1, 1),
        description="Classic Italian pasta dish",
        images=["image1.jpg"],
        category=my_category,
        ingredient_quantities=["200g pasta", "100g bacon"],
        ingredients=["pasta", "bacon", "eggs", "cheese"],
        rating=4.5,
        nutrition=None,
        servings="4",
        recipe_yield="4 portions",
        instructions=["Boil pasta", "Cook bacon", "Mix with eggs"]
    )

@pytest.fixture
def my_nutrition():
    return Nutrition(
        calories=500.0,
        fat_content=20.0,
        saturated_fat_content=8.0,
        cholesterol_content=50.0,
        sodium_content=800.0,
        carbohydrate_content=60.0,
        fiber_content=5.0,
        sugar_content=10.0,
        protein_content=25.0
    )

@pytest.fixture
def my_favourite(my_user, my_recipe):
    return Favourite(my_user.id, my_recipe, datetime(2024, 1, 2))

@pytest.fixture
def my_review(my_user, my_recipe):
    return Review(my_user.id, my_recipe, 4.0, "Delicious!", datetime(2024, 1, 3))

# User tests
def test_user_construction():
    user = User("john_doe", "secret123", 1)
    assert user.id == 1
    assert user.username == "john_doe"
    assert user.password == "secret123"
    assert user.favourite_recipes == []
    assert user.reviews == []

def test_user_construction_without_id():
    user = User("jane_doe", "password456")
    assert user.id is None
    assert user.username == "jane_doe"

def test_user_invalid_username():
    with pytest.raises(ValueError):
        User("", "password123", 1)

def test_user_equality():
    user1 = User("test", "pass", 1)
    user2 = User("test", "pass", 1)
    user3 = User("test", "pass", 2)
    assert user1 == user2
    assert user1 != user3

def test_user_less_than():
    user1 = User("test", "pass", 1)
    user2 = User("test", "pass", 2)
    assert user1 < user2

def test_user_hash():
    user1 = User("test", "pass", 1)
    user2 = User("test", "pass", 1)
    user_set = {user1, user2}
    assert len(user_set) == 1

# Author tests
def test_author_construction():
    author = Author(1, "Jamie Oliver")
    assert author.id == 1
    assert author.name == "Jamie Oliver"
    assert author.recipes == []

def test_author_equality():
    author1 = Author(1, "Chef A")
    author2 = Author(1, "Chef B")
    author3 = Author(2, "Chef A")
    assert author1 == author2
    assert author1 != author3

def test_author_less_than():
    author1 = Author(1, "Chef A")
    author2 = Author(2, "Chef B")
    assert author1 < author2

def test_author_hash():
    author1 = Author(1, "Chef A")
    author2 = Author(1, "Chef B")
    author_set = {author1, author2}
    assert len(author_set) == 1

def test_author_add_recipe(my_author, my_recipe):
    my_author.add_recipe(my_recipe)
    assert my_recipe in my_author.recipes

def test_author_add_duplicate_recipe(my_author, my_recipe):
    my_author.add_recipe(my_recipe)
    with pytest.raises(ValueError):
        my_author.add_recipe(my_recipe)

def test_author_add_invalid_recipe(my_author):
    with pytest.raises(TypeError):
        my_author.add_recipe("not a recipe")

# Category tests
def test_category_construction():
    category = Category("Desserts", [], 1)
    assert category.id == 1
    assert category.name == "Desserts"
    assert category.recipes == []

def test_category_construction_without_id():
    category = Category("Main Course")
    assert category.id is None
    assert category.name == "Main Course"

def test_category_invalid_name():
    with pytest.raises(ValueError):
        Category("", [], 1)

def test_category_equality():
    category1 = Category("Italian", [], 1)
    category2 = Category("French", [], 1)
    category3 = Category("Italian", [], 2)
    assert category1 == category2
    assert category1 != category3

def test_category_less_than():
    category1 = Category("A", [], 1)
    category2 = Category("B", [], 2)
    assert category1 < category2

def test_category_hash():
    category1 = Category("Italian", [], 1)
    category2 = Category("French", [], 1)
    category_set = {category1, category2}
    assert len(category_set) == 1

def test_category_add_recipe(my_category, my_recipe):
    my_category.add_recipe(my_recipe)
    assert my_recipe in my_category.recipes

def test_category_add_invalid_recipe(my_category):
    with pytest.raises(TypeError):
        my_category.add_recipe("not a recipe")

# Recipe tests
def test_recipe_construction(my_author, my_category, my_nutrition):
    recipe = Recipe(
        recipe_id=1,
        name="Test Recipe",
        author=my_author,
        cook_time=30,
        preparation_time=15,
        created_date=datetime(2024, 1, 1),
        description="Test description",
        images=["test.jpg"],
        category=my_category,
        ingredient_quantities=["1 cup flour"],
        ingredients=["flour"],
        rating=4.0,
        nutrition=my_nutrition,
        servings="2",
        recipe_yield="2 portions",
        instructions=["Mix ingredients"]
    )
    assert recipe.id == 1
    assert recipe.name == "Test Recipe"
    assert recipe.author == my_author
    assert recipe.nutrition == my_nutrition

def test_recipe_invalid_id():
    with pytest.raises(ValueError):
        Recipe(0, "Test Recipe", my_author)

def test_recipe_invalid_name(my_author):
    with pytest.raises(ValueError):
        Recipe(1, "", my_author)

def test_recipe_invalid_author():
    with pytest.raises(ValueError):
        Recipe(1, "Test Recipe", None)

def test_recipe_setters(my_recipe):
    my_recipe.cook_time = 40
    assert my_recipe.cook_time == 40
    my_recipe.preparation_time = 20
    assert my_recipe.preparation_time == 20
    my_recipe.description = "New description"
    assert my_recipe.description == "New description"
    my_recipe.images = ["new.jpg"]
    assert my_recipe.images == ["new.jpg"]
    my_recipe.rating = 3.5
    assert my_recipe.rating == 3.5
    my_recipe.servings = "3"
    assert my_recipe.servings == "3"
    my_recipe.recipe_yield = "3 portions"
    assert my_recipe.recipe_yield == "3 portions"
    my_recipe.instructions = ["New step"]
    assert my_recipe.instructions == ["New step"]

def test_recipe_invalid_setters(my_recipe):
    with pytest.raises(ValueError):
        my_recipe.cook_time = -1
    with pytest.raises(ValueError):
        my_recipe.preparation_time = -1
    with pytest.raises(ValueError):
        my_recipe.rating = 6.0
    with pytest.raises(TypeError):
        my_recipe.images = ["image", 123]
    with pytest.raises(ValueError):
        my_recipe.instructions = "not a list"

def test_recipe_equality(my_author):
    recipe1 = Recipe(1, "Recipe A", my_author)
    recipe2 = Recipe(1, "Recipe B", my_author)
    recipe3 = Recipe(2, "Recipe A", my_author)
    assert recipe1 == recipe2
    assert recipe1 != recipe3

def test_recipe_less_than(my_author):
    recipe1 = Recipe(1, "Recipe A", my_author)
    recipe2 = Recipe(2, "Recipe B", my_author)
    assert recipe1 < recipe2

def test_recipe_hash(my_author):
    recipe1 = Recipe(1, "Recipe A", my_author)
    recipe2 = Recipe(1, "Recipe B", my_author)
    recipe_set = {recipe1, recipe2}
    assert len(recipe_set) == 1

# Nutrition tests
def test_nutrition_construction(my_nutrition):
    assert my_nutrition.calories == 500.0
    assert my_nutrition.fat_content == 20.0
    assert my_nutrition.saturated_fat_content == 8.0
    assert my_nutrition.cholesterol_content == 50.0
    assert my_nutrition.sodium_content == 800.0
    assert my_nutrition.carbohydrate_content == 60.0
    assert my_nutrition.fiber_content == 5.0
    assert my_nutrition.sugar_content == 10.0
    assert my_nutrition.protein_content == 25.0

def test_nutrition_setters(my_nutrition):
    my_nutrition.calories = 600.0
    assert my_nutrition.calories == 600.0
    my_nutrition.fat_content = None
    assert my_nutrition.fat_content is None
    my_nutrition.saturated_fat_content = 10.0
    assert my_nutrition.saturated_fat_content == 10.0
    my_nutrition.cholesterol_content = 60.0
    assert my_nutrition.cholesterol_content == 60.0
    my_nutrition.sodium_content = 900.0
    assert my_nutrition.sodium_content == 900.0
    my_nutrition.carbohydrate_content = 70.0
    assert my_nutrition.carbohydrate_content == 70.0
    my_nutrition.fiber_content = 6.0
    assert my_nutrition.fiber_content == 6.0
    my_nutrition.sugar_content = 12.0
    assert my_nutrition.sugar_content == 12.0
    my_nutrition.protein_content = 30.0
    assert my_nutrition.protein_content == 30.0

def test_nutrition_invalid_setters(my_nutrition):
    with pytest.raises(ValueError):
        my_nutrition.calories = -1.0
    with pytest.raises(ValueError):
        my_nutrition.fat_content = -1.0
    with pytest.raises(ValueError):
        my_nutrition.saturated_fat_content = -1.0
    with pytest.raises(ValueError):
        my_nutrition.cholesterol_content = -1.0
    with pytest.raises(ValueError):
        my_nutrition.sodium_content = -1.0
    with pytest.raises(ValueError):
        my_nutrition.carbohydrate_content = -1.0
    with pytest.raises(ValueError):
        my_nutrition.fiber_content = -1.0
    with pytest.raises(ValueError):
        my_nutrition.sugar_content = -1.0
    with pytest.raises(ValueError):
        my_nutrition.protein_content = -1.0

def test_nutrition_equality():
    nutrition1 = Nutrition(calories=500.0, fat_content=20.0)
    nutrition2 = Nutrition(calories=500.0, fat_content=20.0)
    nutrition3 = Nutrition(calories=600.0, fat_content=20.0)
    assert nutrition1 == nutrition2
    assert nutrition1 != nutrition3

def test_nutrition_hash():
    nutrition1 = Nutrition(calories=500.0, fat_content=20.0)
    nutrition2 = Nutrition(calories=500.0, fat_content=20.0)
    nutrition_set = {nutrition1, nutrition2}
    assert len(nutrition_set) == 1

# Favourite tests
def test_favourite_construction(my_favourite):
    assert my_favourite.user_id == "1"
    assert my_favourite.recipe.name == "Spaghetti Carbonara"
    assert my_favourite.created_date == datetime(2024, 1, 2)

def test_favourite_invalid_user_id(my_recipe):
    with pytest.raises(ValueError):
        Favourite("", my_recipe)

def test_favourite_invalid_recipe(my_user):
    with pytest.raises(ValueError):
        Favourite(my_user.id, "not a recipe")

def test_favourite_equality(my_user, my_recipe):
    favourite1 = Favourite(my_user.id, my_recipe, datetime(2024, 1, 2))
    favourite2 = Favourite(my_user.id, my_recipe, datetime(2024, 1, 2))
    favourite3 = Favourite("2", my_recipe, datetime(2024, 1, 2))
    assert favourite1 == favourite2
    assert favourite1 != favourite3

def test_favourite_hash(my_user, my_recipe):
    favourite1 = Favourite(my_user.id, my_recipe, datetime(2024, 1, 2))
    favourite2 = Favourite(my_user.id, my_recipe, datetime(2024, 1, 2))
    favourite_set = {favourite1, favourite2}
    assert len(favourite_set) == 1

def test_favourite_setter(my_favourite):
    new_date = datetime(2024, 2, 1)
    my_favourite.created_date = new_date
    assert my_favourite.created_date == new_date

def test_favourite_invalid_setter(my_favourite):
    with pytest.raises(TypeError):
        my_favourite.created_date = "not a datetime"

# Review tests
def test_review_construction(my_review):
    assert my_review.user_id == "1"
    assert my_review.recipe.name == "Spaghetti Carbonara"
    assert my_review.rating == 4.0
    assert my_review.comment == "Delicious!"
    assert my_review.created_date == datetime(2024, 1, 3)

def test_review_invalid_user_id(my_recipe):
    with pytest.raises(ValueError):
        Review("", my_recipe, 4.0)

def test_review_invalid_recipe(my_user):
    with pytest.raises(ValueError):
        Review(my_user.id, "not a recipe", 4.0)

def test_review_invalid_rating(my_user, my_recipe):
    with pytest.raises(ValueError):
        Review(my_user.id, my_recipe, 6.0)
    with pytest.raises(ValueError):
        Review(my_user.id, my_recipe, -1.0)

def test_review_equality(my_user, my_recipe):
    review1 = Review(my_user.id, my_recipe, 4.0, "Great", datetime(2024, 1, 3))
    review2 = Review(my_user.id, my_recipe, 4.0, "Great", datetime(2024, 1, 3))
    review3 = Review("2", my_recipe, 4.0, "Great", datetime(2024, 1, 3))
    assert review1 == review2
    assert review1 != review3

def test_review_hash(my_user, my_recipe):
    review1 = Review(my_user.id, my_recipe, 4.0, datetime(2024, 1, 3))
    review2 = Review(my_user.id, my_recipe, 4.0, datetime(2024, 1, 3))
    review_set = {review1, review2}
    assert len(review_set) == 1

def test_review_setters(my_review):
    my_review.rating = 5.0
    assert my_review.rating == 5.0
    my_review.comment = "Amazing!"
    assert my_review.comment == "Amazing!"
    new_date = datetime(2024, 2, 1)
    my_review.created_date = new_date
    assert my_review.created_date == new_date

def test_review_invalid_setters(my_review):
    with pytest.raises(ValueError):
        my_review.rating = 6.0
    with pytest.raises(TypeError):
        my_review.created_date = "not a datetime"

def test_recipe_reviews(my_recipe, my_user):
    review1 = Review(my_user.id, my_recipe, 4.0, "Good")
    review2 = Review("2", my_recipe, 5.0, "Great")
    my_recipe.add_review(review1)
    my_recipe.add_review(review2)
    assert my_recipe.rating == 4.5
    my_recipe.remove_review(review1)
    assert my_recipe.rating == 5.0
    with pytest.raises(ValueError):
        my_recipe.remove_review(review1)
    with pytest.raises(TypeError):
        my_recipe.add_review("not a review")