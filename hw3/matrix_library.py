from typing import Union


class Matrix:
    def __init__(self, matrix: list[list[Union[float, int]]]):
        self.matrix = matrix

    def __getitem__(self, idx):
        return self.matrix[idx]

    @property
    def shape(self):
        return len(self.matrix), len(self.matrix[0])

    def _shape_check(self, other_matrix, dot_product: bool = False):
        # check all rows have the same number of columns
        for i in range(1, other_matrix.shape[0]):
            if len(other_matrix.matrix[i]) != other_matrix.shape[1]:
                raise AssertionError("All rows in a matrix should have the same number of columns.")

        # shapes a matched for A @ B
        if dot_product:
            a_rows = self.shape[0]
            b_cols = other_matrix.shape[1]
            if a_rows != b_cols:
                raise ValueError(f"Can not conduct matrix multiplication, check matrix shape: "
                                 f"{self.shape} and {other_matrix.shape}")
        # shapes are matched for A + B or A * B
        else:
            if self.shape != other_matrix.shape:
                raise ValueError(f"Can not add matrices of different shapes"
                                 " got matrices of shape: {self.shape} and {other_matrix.shape}")

    @staticmethod
    def _get_rows_multiplication(row1, row2):
        return sum([i * j for i, j in zip(row1, row2)])

    @staticmethod
    def _get_column(matrix, idx):
        return [matrix[i][idx] for i in range(matrix.shape[0])]

    def __add__(self, other_matrix):
        self._shape_check(other_matrix)
        rows_num, cols_num = other_matrix.shape
        result_sum = []
        for i in range(rows_num):
            _result_sum = []
            for j in range(cols_num):
                _result_sum.append(self[i][j] + other_matrix[i][j])
            result_sum.append(_result_sum)
        return Matrix(result_sum)

    def __mul__(self, other_matrix):
        self._shape_check(other_matrix)
        rows_num, cols_num = other_matrix.shape
        result_sum = []
        for i in range(rows_num):
            _result_sum = []
            for j in range(cols_num):
                _result_sum.append(self[i][j] * other_matrix[i][j])
            result_sum.append(_result_sum)
        return Matrix(result_sum)

    def __matmul__(self, other_matrix):
        self._shape_check(other_matrix, dot_product=True)
        result_sum = []
        n_rows = self.shape[0]
        n_cols = other_matrix.shape[1]
        for i in range(n_rows):
            _result_sum = []
            for j in range(n_cols):
                _result_sum.append(self._get_rows_multiplication(self[i], self._get_column(other_matrix, j)))
            result_sum.append(_result_sum)
        return Matrix(result_sum)

    def __str__(self):
        return "\n".join(["\t".join([str(cell) for cell in row]) for row in self])
