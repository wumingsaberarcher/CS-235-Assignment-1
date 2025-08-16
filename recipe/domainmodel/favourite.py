from typing import Optional
from datetime import datetime
from recipe.domainmodel.recipe import Recipe

class Favourite:
    def __init__(self, user_id: str, recipe: Recipe, created_date: Optional[datetime] = None):
        """
        Initialize a Favourite instance representing a user's favorite recipe.

        Args:
            user_id (str): Unique identifier for the user who favorited the recipe.
            recipe (Recipe): The recipe instance that is favorited.
            created_date (Optional[datetime]): The date and time when the recipe was favorited.
                                             Defaults to current time if not provided.

        Raises:
            ValueError: If user_id is empty or not a string, or if recipe is not a Recipe instance.
        """
        if not isinstance(user_id, str) or not user_id.strip():
            raise ValueError("user_id must be a non-empty string.")
        if not isinstance(recipe, Recipe):
            raise ValueError("recipe must be a Recipe instance.")

        self.__user_id = user_id
        self.__recipe = recipe
        self.__created_date = created_date if created_date else datetime.now()

    def __repr__(self) -> str:
        """
        Return a string representation of the Favourite instance.

        Returns:
            str: A string describing the user, recipe, and date favorited.
        """
        return (f"<Favourite user_id={self.__user_id}, recipe={self.__recipe.name}, "
                f"favorited on {self.__created_date}>")

    def __eq__(self, other) -> bool:
        """
        Check if two Favourite instances are equal based on user_id and recipe.

        Args:
            other: Another object to compare with.

        Returns:
            bool: True if the objects are equal, False otherwise.
        """
        if not isinstance(other, Favourite):
            return False
        return self.__user_id == other.user_id and self.__recipe == other.recipe

    def __hash__(self) -> int:
        """
        Return a hash value for the Favourite instance.

        Returns:
            int: Hash value based on user_id and recipe.
        """
        return hash((self.__user_id, self.__recipe))

    @property
    def user_id(self) -> str:
        """Get the user ID who favorited the recipe."""
        return self.__user_id

    @property
    def recipe(self) -> Recipe:
        """Get the favorited recipe."""
        return self.__recipe

    @property
    def created_date(self) -> datetime:
        """Get the date and time when the recipe was favorited."""
        return self.__created_date

    @created_date.setter
    def created_date(self, value: datetime):
        """Set the date and time when the recipe was favorited.

        Args:
            value (datetime): The date and time to set.

        Raises:
            TypeError: If value is not a datetime instance.
        """
        if not isinstance(value, datetime):
            raise TypeError("created_date must be a datetime instance.")
        self.__created_date = value