import numpy as np
from numbers import Number
from numpy.lib.mixins import NDArrayOperatorsMixin


class FileWriter:
    def save_matrix_to_txt(self, filepath: str) -> None:
        with open(filepath, "w") as f:
            f.write(self.__str__())


class StringTransformer:
    def __str__(self):
        return "\n".join(["\t".join([str(cell) for cell in row]) for row in self.values])


class GetValue:
    def __init__(self, data):
        self.values = data

    @property
    def values(self):
        return self.__values

    @values.setter
    def values(self, value):
        self.__values = value


class MatrixArithmeticOperations(NDArrayOperatorsMixin, GetValue, StringTransformer, FileWriter):
    _HANDLED_TYPES = (np.ndarray, Number)

    def __array_ufunc__(self, ufunc, method, *args, **kwargs):
        for x in args:
            if not isinstance(x, self._HANDLED_TYPES + (MatrixArithmeticOperations,)):
                return NotImplemented("This operation is not supported.")
        args = (x.values for x in args)

        return type(self)(getattr(ufunc, method)(*args, **kwargs))
