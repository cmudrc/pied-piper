from __future__ import annotations
from collections.abc import Iterator


class Resource:
    """
    Container for resource quantities used in the simulation.

    The ``Resource`` class provides a lightweight, validated wrapper around the
    default resource types used in PiperABM (``food``, ``water``, ``energy``).
    It supports arithmetic operations and can be converted to a plain dictionary
    for storage on NetworkX graph nodes.

    Notes
    -----
    Internally, PiperABM stores resources as dictionaries attached directly to
    NetworkX graph nodes. The ``Resource`` class is provided as an optional
    convenience wrapper for validation, readability, and arithmetic operations.
    """

    def __init__(self, food: float = 0, water: float = 0, energy: float = 0):
        """
        Initialize a Resource instance.

        Parameters
        ----------
        food : float, optional
            Amount of food resource. Must be non-negative.

        water : float, optional
            Amount of water resource. Must be non-negative.

        energy : float, optional
            Amount of energy resource. Must be non-negative.

        Raises
        ------
        ValueError
            If any resource value is negative.
        """
        if food < 0 or water < 0 or energy < 0:
            raise ValueError("Resource values cannot be negative.")
        self.food = food
        self.water = water
        self.energy = energy

    # --- Mapping/iterable behavior (enables dict(Resource(...))) ---
    def __iter__(self) -> Iterator[tuple[str, float]]:
        yield "food", self.food
        yield "water", self.water
        yield "energy", self.energy

    def __len__(self) -> int:
        return 3

    def __getitem__(self, key: str) -> float:
        if key == "food":
            return self.food
        if key == "water":
            return self.water
        if key == "energy":
            return self.energy
        raise KeyError(key)

    def serialize(self):
        """
        Convert the resource object to a dictionary.

        Returns
        -------
        dict
            Dictionary representation of the resource with keys
            ``'food'``, ``'water'``, and ``'energy'``.
        """
        return {
            "food": self.food,
            "water": self.water,
            "energy": self.energy,
        }
    
    def __add__(self, other: dict | Resource):
        """
        Add resources element-wise.

        Parameters
        ----------
        other : dict or Resource
            Resource values to add. If a dictionary is provided, missing
            resource keys default to zero.

        Returns
        -------
        Resource
            New ``Resource`` instance containing the summed values.

        Raises
        ------
        TypeError
            If ``other`` is not a ``dict`` or ``Resource``.
        """
        if isinstance(other, Resource):
            return Resource(
                food=self.food + other.food,
                water=self.water + other.water,
                energy=self.energy + other.energy,
            )
        elif isinstance(other, dict):
            return Resource(
                food=self.food + other.get("food", 0),
                water=self.water + other.get("water", 0),
                energy=self.energy + other.get("energy", 0),
            )
        else:
            raise TypeError("Unsupported type for addition.")
        
    def __sub__(self, other: dict | Resource):
        """
        Subtract resources element-wise.

        Parameters
        ----------
        other : dict or Resource
            Resource values to subtract. If a dictionary is provided, missing
            resource keys default to zero.

        Returns
        -------
        Resource
            New ``Resource`` instance containing the subtracted values.

        Raises
        ------
        TypeError
            If ``other`` is not a ``dict`` or ``Resource``.
        """
        if isinstance(other, Resource):
            return Resource(
                food=self.food - other.food,
                water=self.water - other.water,
                energy=self.energy - other.energy,
            )
        elif isinstance(other, dict):
            return Resource(
                food=self.food - other.get("food", 0),
                water=self.water - other.get("water", 0),
                energy=self.energy - other.get("energy", 0),
            )
        else:
            raise TypeError("Unsupported type for addition.")
    
    def __mul__(self, other: int | float | dict):
        """
        Multiply resources element-wise or by a scalar.

        Parameters
        ----------
        other : int, float, or dict
            Scalar multiplier or dictionary of per-resource multipliers.
            Missing keys in dictionaries default to ``1``.

        Returns
        -------
        Resource
            New ``Resource`` instance containing the scaled values.

        Raises
        ------
        TypeError
            If ``other`` is not a supported type.
        """
        if isinstance(other, (int, float)):
            return Resource(
                food=self.food * other,
                water=self.water * other,
                energy=self.energy * other,
            )
        elif isinstance(other, dict):
            return Resource(
                food=self.food * other.get("food", 1),
                water=self.water * other.get("water", 1),
                energy=self.energy * other.get("energy", 1),
            )
        else:
            raise TypeError("Unsupported type for multiplication.")

    def __truediv__(self, other: int | float | dict):
        """
        Divide resources element-wise or by a scalar.

        Parameters
        ----------
        other : int, float, or dict
            Scalar divisor or dictionary of per-resource divisors.
            Missing keys in dictionaries default to ``1``.

        Returns
        -------
        Resource
            New ``Resource`` instance containing the divided values.

        Raises
        ------
        TypeError
            If ``other`` is not a supported type.
        """
        if isinstance(other, (int, float)):
            return Resource(
                food=self.food / other,
                water=self.water / other,
                energy=self.energy / other,
            )
        elif isinstance(other, dict):
            return Resource(
                food=self.food / other.get("food", 1),
                water=self.water / other.get("water", 1),
                energy=self.energy / other.get("energy", 1),
            )
        else:
            raise TypeError("Unsupported type for division.")
    

if __name__ == "__main__":
    resource = Resource(food=10, water=20, energy=30)
    print(resource.serialize())
