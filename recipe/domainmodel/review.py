from typing import Optional
from datetime import datetime
from recipe.domainmodel.recipe import Recipe

class Review:
    def __init__(self, user_id: str, recipe: Recipe, rating: float, comment: Optional[str] = None, created_date: Optional[datetime] = None):
        """
        Initialize a Review instance representing a user's review of a recipe.

        Args:
            user_id (str): Unique identifier for the user who created the review.
            recipe (Recipe): The recipe instance being reviewed.
            rating (float): The rating given to the recipe (between 0 and 5).
            comment (Optional[str]): An optional comment provided with the review.
            created_date (Optional[datetime]): The date and time when the review was created.
                                             Defaults to current time if not provided.

        Raises:
            ValueError: If user_id is empty or not a string, recipe is not a Recipe instance,
                        or rating is not between 0 and 5.
        """
        if not isinstance(user_id, str) or not user_id.strip():
            raise ValueError("user_id must be a non-empty string.")
        if not isinstance(recipe, Recipe):
            raise ValueError("recipe must be a Recipe instance.")
        if not isinstance(rating, (int, float)) or rating < 0 or rating > 5:
            raise ValueError("rating must be a number between 0 and 5.")

        self.__user_id = user_id
        self.__recipe = recipe
        self.__rating = float(rating)
        self.__comment = comment.strip() if comment else None
        self.__created_date = created_date if created_date else datetime.now()

    def __repr__(self) -> str:
        """
        Return a string representation of the Review instance.

        Returns:
            str: A string describing the user, recipe, rating, and date of the review.
        """
        return (f"<Review user_id={self.__user_id}, recipe={self.__recipe.name}, "
                f"rating={self.__rating}, created on {self.__created_date}>")

    def __eq__(self, other) -> bool:
        """
        Check if two Review instances are equal based on user_id, recipe, and created_date.

        Args:
            other: Another object to compare with.

        Returns:
            bool: True if the objects are equal, False otherwise.
        """
        if not isinstance(other, Review):
            return False
        return (self.__user_id == other.user_id and
                self.__recipe == other.recipe and
                self.__created_date == other.created_date)

    def __hash__(self) -> int:
        """
        Return a hash value for the Review instance.

        Returns:
            int: Hash value based on user_id, recipe, and created_date.
        """
        return hash((self.__user_id, self.__recipe, self.__created_date))

    @property
    def user_id(self) -> str:
        """Get the user ID of the reviewer."""
        return self.__user_id

    @property
    def recipe(self) -> Recipe:
        """Get the reviewed recipe."""
        return self.__recipe

    @property
    def rating(self) -> float:
        """Get the rating given to the recipe."""
        return self.__rating

    @rating.setter
    def rating(self, value: float):
        """Set the rating for the review.

        Args:
            value (float): The rating to set (between 0 and 5).

        Raises:
            ValueError: If the rating is not between 0 and 5.
        """
        if not isinstance(value, (int, float)) or value < 0 or value > 5:
            raise ValueError("rating must be a number between 0 and 5.")
        self.__rating = float(value)

    @property
    def comment(self) -> Optional[str]:
        """Get the comment provided with the review."""
        return self.__comment

    @comment.setter
    def comment(self, value: Optional[str]):
        """Set the comment for the review.

        Args:
            value (Optional[str]): The comment to set.
        """
        self.__comment = value.strip() if value else None

    @property
    def created_date(self) -> datetime:
        """Get the date and time when the review was created."""
        return self.__created_date

    @created_date.setter
    def created_date(self, value: datetime):
        """Set the date and time when the review was created.

        Args:
            value (datetime): The date and time to set.

        Raises:
            TypeError: If value is not a datetime instance.
        """
        if not isinstance(value, datetime):
            raise TypeError("created_date must be a datetime instance.")
        self.__created_date = value