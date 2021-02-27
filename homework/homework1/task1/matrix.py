from typing import List, Union

from homework.homework1.task1.vector import Vector


class Matrix:
    __matrix: List[List[Union[int, float]]]

    def __init__(self, *matrix: List[Union[int, float]]) -> None:
        if not matrix:
            raise ValueError("Matrix must contain at least one element.")

        length = len(matrix[0])

        if length == 0:
            raise ValueError("Matrix rows must not be empty.")

        for row in matrix:
            if len(row) != length:
                raise ValueError("Matrix rows must be the same length.")

        self.__matrix = list(matrix)

    def __eq__(self, other) -> bool:
        return isinstance(other, Matrix) and self.__matrix == other.__matrix

    def __str__(self) -> str:
        output = ""
        for row in self.__matrix:
            output += " ".join(map(str, row)) + "\n"
        return output.strip("\n")

    def __add__(self, other: "Matrix") -> "Matrix":
        if not self.__are_dimensions_equal(other):
            raise ValueError("Matrices do not have the same dimensions.")

        return Matrix(
            *[
                list(map(lambda x, y: x + y, zip(self.__matrix[i], other.__matrix[i])))
                for i in range(self.__number_of_rows())
            ]
        )

    def __mul__(self, other: "Matrix") -> "Matrix":
        if not self.__can_be_multiplied(other):
            raise ValueError("Matrices have incompatible dimensions.")

        return Matrix(
            *[
                [
                    Vector(*self.__matrix[i]).dot(Vector(*other.transpose().__matrix[j]))
                    for j in range(other.__number_of_columns())
                ]
                for i in range(self.__number_of_rows())
            ]
        )

    def transpose(self) -> "Matrix":
        return Matrix(*[list(x) for x in zip(*self.__matrix)])

    def __number_of_columns(self) -> int:
        return len(self.__matrix[0])

    def __number_of_rows(self) -> int:
        return len(self.__matrix)

    def __are_dimensions_equal(self, other: "Matrix") -> bool:
        return (
            self.__number_of_rows() == other.__number_of_rows()
            and self.__number_of_columns() == other.__number_of_columns()
        )

    def __can_be_multiplied(self, other: "Matrix") -> bool:
        return self.__number_of_columns() == other.__number_of_rows()
