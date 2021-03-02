from math import sqrt, acos, degrees
from typing import List


class Vector:
    __elements: List[float]

    def __init__(self, *elements: float) -> None:
        if not elements:
            raise ValueError("The vector must contain at least one element.")

        self.__elements = list(elements)

    def __str__(self) -> str:
        return f"({', '.join(map(str, self.__elements))})"

    def dot(self, other: "Vector") -> float:
        if len(self.__elements) != len(other.__elements):
            raise ValueError("The dimensions of the vectors do not match.")

        return sum(x * y for x, y in zip(self.__elements, other.__elements))

    def norm(self) -> float:
        return sqrt(self.dot(self))

    def angle(self, other: "Vector") -> float:
        return degrees(acos(self.dot(other) / (self.norm() * other.norm())))
