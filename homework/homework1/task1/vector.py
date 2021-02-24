from math import sqrt, acos, degrees


class Vector:
    __elements: list[int]

    def __init__(self, *elements: int):
        if not elements:
            raise ValueError("The vector must contain at least one element.")

        self.__elements = list(elements)

    def __str__(self):
        return str(self.__elements)

    def dot(self, other: "Vector"):
        if len(self.__elements) != len(other.__elements):
            raise ValueError("The dimensions of the vectors do not match.")

        return sum(x * y for x, y in zip(self.__elements, other.__elements))

    def norm(self):
        return sqrt(self.dot(self))

    def angle(self, other: "Vector"):
        return degrees(acos(self.dot(other) / self.norm() / other.norm()))