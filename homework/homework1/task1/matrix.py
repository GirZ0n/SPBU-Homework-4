class Matrix:
    __matrix: list[list[int]]

    def __init__(self, *matrix: list[int]):
        if not matrix:
            raise ValueError("The matrix must contain at least one element.")

        length = len(matrix[0])
        for row in matrix:
            if len(row) != length:
                raise ValueError("Matrix rows must be the same length.")

        self.__matrix = list(matrix)

    def __eq__(self, other):
        return isinstance(other, Matrix) and self.__matrix == other.__matrix

    def __str__(self):
        output = ""
        for row in self.__matrix:
            output += " ".join(map(str, row)) + "\n"
        return output.strip("\n")

    def __add__(self, other: "Matrix"):
        if not self.__are_dimensions_equal(other):
            raise ValueError("Matrices do not have the same dimensions.")

        new_matrix = list()
        for i in range(self.__number_of_rows()):
            row = list()
            for j in range(self.__number_of_columns()):
                row.append(self.__matrix[i][j] + other.__matrix[i][j])
            new_matrix.append(row)

        return Matrix(*new_matrix)

    def __mul__(self, other: "Matrix"):
        if not self.__can_be_multiplied(other):
            raise ValueError("Matrices have incompatible dimensions.")

        result = list()
        for i in range(self.__number_of_rows()):
            row = list()
            for j in range(other.__number_of_columns()):
                total = 0
                for k in range(other.__number_of_rows()):
                    total += self.__matrix[i][k] * other.__matrix[k][j]
                row.append(total)
            result.append(row)

        return Matrix(*result)

    def transpose(self):
        transposed_array = list()

        for j in range(self.__number_of_columns()):
            row = list()
            for i in range(self.__number_of_rows()):
                row.append(self.__matrix[i][j])
            transposed_array.append(row)

        return Matrix(*transposed_array)

    def __number_of_columns(self):
        return len(self.__matrix[0])

    def __number_of_rows(self):
        return len(self.__matrix)

    def __are_dimensions_equal(self, other: "Matrix"):
        return (
            self.__number_of_rows() == other.__number_of_rows()
            and self.__number_of_columns() == other.__number_of_columns()
        )

    def __can_be_multiplied(self, other: "Matrix"):
        return self.__number_of_columns() == other.__number_of_rows()
