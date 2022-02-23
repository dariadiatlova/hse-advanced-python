import numpy as np

from hw3 import HW3_ROOT_PATH
from hw3.numpy_matrix_library import MatrixArithmeticOperations

np.random.seed(0)


def test_medium_task(txt_save_path: str = f"{HW3_ROOT_PATH}/artifacts/medium"):
    sample1 = np.random.randint(0, 10, (10, 10))
    sample2 = np.random.randint(0, 10, (10, 10))

    matrix1 = MatrixArithmeticOperations(sample1.tolist())
    matrix2 = MatrixArithmeticOperations(sample2.tolist())

    addition = matrix1 + matrix2
    point_wise_multiplication = matrix1 * matrix2
    dot_product = matrix1 @ matrix2

    assert np.array_equal(addition.values, sample1 + sample2), "Sum of matrices is incorrect!"
    assert np.array_equal(point_wise_multiplication.values, sample1 * sample2), \
        "Point-wise multiplication of matrices is incorrect!"
    assert np.array_equal(dot_product.values, sample1 @ sample2), "Dot product of matrices is incorrect!"

    addition.save_matrix_to_txt(f"{txt_save_path}/matrix+.txt")
    point_wise_multiplication.save_matrix_to_txt(f"{txt_save_path}/matrix*.txt")
    dot_product.save_matrix_to_txt(f"{txt_save_path}/matrix@.txt")
