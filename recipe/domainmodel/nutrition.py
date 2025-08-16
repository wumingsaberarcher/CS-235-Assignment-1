from recipe.domainmodel.recipe import Recipe

from typing import Optional

class Nutrition:
    def __init__(
        self,
        calories: Optional[float] = None,
        fat_content: Optional[float] = None,
        saturated_fat_content: Optional[float] = None,
        cholesterol_content: Optional[float] = None,
        sodium_content: Optional[float] = None,
        carbohydrate_content: Optional[float] = None,
        fiber_content: Optional[float] = None,
        sugar_content: Optional[float] = None,
        protein_content: Optional[float] = None
    ):
        """
        Initialize a Nutrition instance with nutritional information.

        Args:
            calories (Optional[float]): Total calories in the recipe (kcal).
            fat_content (Optional[float]): Total fat content (grams).
            saturated_fat_content (Optional[float]): Saturated fat content (grams).
            cholesterol_content (Optional[float]): Cholesterol content (milligrams).
            sodium_content (Optional[float]): Sodium content (milligrams).
            carbohydrate_content (Optional[float]): Total carbohydrate content (grams).
            fiber_content (Optional[float]): Dietary fiber content (grams).
            sugar_content (Optional[float]): Sugar content (grams).
            protein_content (Optional[float]): Protein content (grams).
        """
        self.__calories = calories
        self.__fat_content = fat_content
        self.__saturated_fat_content = saturated_fat_content
        self.__cholesterol_content = cholesterol_content
        self.__sodium_content = sodium_content
        self.__carbohydrate_content = carbohydrate_content
        self.__fiber_content = fiber_content
        self.__sugar_content = sugar_content
        self.__protein_content = protein_content

    def __repr__(self) -> str:
        """
        Return a string representation of the Nutrition instance.

        Returns:
            str: A string describing the nutritional information.
        """
        return (f"<Nutrition calories={self.__calories}, fat={self.__fat_content}g, "
                f"saturated_fat={self.__saturated_fat_content}g, cholesterol={self.__cholesterol_content}mg, "
                f"sodium={self.__sodium_content}mg, carbs={self.__carbohydrate_content}g, "
                f"fiber={self.__fiber_content}g, sugar={self.__sugar_content}g, protein={self.__protein_content}g>")

    def __eq__(self, other) -> bool:
        """
        Check if two Nutrition instances are equal based on their attributes.

        Args:
            other: Another object to compare with.

        Returns:
            bool: True if the objects are equal, False otherwise.
        """
        if not isinstance(other, Nutrition):
            return False
        return (
            self.__calories == other.calories and
            self.__fat_content == other.fat_content and
            self.__saturated_fat_content == other.saturated_fat_content and
            self.__cholesterol_content == other.cholesterol_content and
            self.__sodium_content == other.sodium_content and
            self.__carbohydrate_content == other.carbohydrate_content and
            self.__fiber_content == other.fiber_content and
            self.__sugar_content == other.sugar_content and
            self.__protein_content == other.protein_content
        )

    def __hash__(self) -> int:
        """
        Return a hash value for the Nutrition instance.

        Returns:
            int: Hash value based on nutritional attributes.
        """
        return hash((
            self.__calories,
            self.__fat_content,
            self.__saturated_fat_content,
            self.__cholesterol_content,
            self.__sodium_content,
            self.__carbohydrate_content,
            self.__fiber_content,
            self.__sugar_content,
            self.__protein_content
        ))

    @property
    def calories(self) -> Optional[float]:
        """Get the total calories (kcal)."""
        return self.__calories

    @calories.setter
    def calories(self, value: Optional[float]):
        """Set the total calories, ensuring non-negative values or None."""
        if value is not None and value < 0:
            raise ValueError("Calories cannot be negative.")
        self.__calories = value

    @property
    def fat_content(self) -> Optional[float]:
        """Get the total fat content (grams)."""
        return self.__fat_content

    @fat_content.setter
    def fat_content(self, value: Optional[float]):
        """Set the total fat content, ensuring non-negative values or None."""
        if value is not None and value < 0:
            raise ValueError("Fat content cannot be negative.")
        self.__fat_content = value

    @property
    def saturated_fat_content(self) -> Optional[float]:
        """Get the saturated fat content (grams)."""
        return self.__saturated_fat_content

    @saturated_fat_content.setter
    def saturated_fat_content(self, value: Optional[float]):
        """Set the saturated fat content, ensuring non-negative values or None."""
        if value is not None and value < 0:
            raise ValueError("Saturated fat content cannot be negative.")
        self.__saturated_fat_content = value

    @property
    def cholesterol_content(self) -> Optional[float]:
        """Get the cholesterol content (milligrams)."""
        return self.__cholesterol_content

    @cholesterol_content.setter
    def cholesterol_content(self, value: Optional[float]):
        """Set the cholesterol content, ensuring non-negative values or None."""
        if value is not None and value < 0:
            raise ValueError("Cholesterol content cannot be negative.")
        self.__cholesterol_content = value

    @property
    def sodium_content(self) -> Optional[float]:
        """Get the sodium content (milligrams)."""
        return self.__sodium_content

    @sodium_content.setter
    def sodium_content(self, value: Optional[float]):
        """Set the sodium content, ensuring non-negative values or None."""
        if value is not None and value < 0:
            raise ValueError("Sodium content cannot be negative.")
        self.__sodium_content = value

    @property
    def carbohydrate_content(self) -> Optional[float]:
        """Get the total carbohydrate content (grams)."""
        return self.__carbohydrate_content

    @carbohydrate_content.setter
    def carbohydrate_content(self, value: Optional[float]):
        """Set the carbohydrate content, ensuring non-negative values or None."""
        if value is not None and value < 0:
            raise ValueError("Carbohydrate content cannot be negative.")
        self.__carbohydrate_content = value

    @property
    def fiber_content(self) -> Optional[float]:
        """Get the dietary fiber content (grams)."""
        return self.__fiber_content

    @fiber_content.setter
    def fiber_content(self, value: Optional[float]):
        """Set the fiber content, ensuring non-negative values or None."""
        if value is not None and value < 0:
            raise ValueError("Fiber content cannot be negative.")
        self.__fiber_content = value

    @property
    def sugar_content(self) -> Optional[float]:
        """Get the sugar content (grams)."""
        return self.__sugar_content

    @sugar_content.setter
    def sugar_content(self, value: Optional[float]):
        """Set the sugar content, ensuring non-negative values or None."""
        if value is not None and value < 0:
            raise ValueError("Sugar content cannot be negative.")
        self.__sugar_content = value

    @property
    def protein_content(self) -> Optional[float]:
        """Get the protein content (grams)."""
        return self.__protein_content

    @protein_content.setter
    def protein_content(self, value: Optional[float]):
        """Set the protein content, ensuring non-negative values or None."""
        if value is not None and value < 0:
            raise ValueError("Protein content cannot be negative.")
        self.__protein_content = value