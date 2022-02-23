import numpy as np

from hw3 import HW3_ROOT_PATH
from hw3.matrix_library import Matrix
from hw3.utils import save_matrix_to_txt

np.random.seed(0)


def test_easy_task(txt_save_path: str = f"{HW3_ROOT_PATH}/artifacts/easy"):
    sample1 = np.random.randint(0, 10, (10, 10))
    sample2 = np.random.randint(0, 10, (10, 10))

    matrix1 = Matrix(sample1.tolist())
    matrix2 = Matrix(sample2.tolist())

    addition = matrix1 + matrix2
    point_wise_multiplication = matrix1 * matrix2
    dot_product = matrix1 @ matrix2

    assert addition.matrix == (sample1 + sample2).tolist(), "Sum of matrices is incorrect!"
    assert point_wise_multiplication.matrix == (sample1 * sample2).tolist(), \
        "Point-wise multiplication of matrices is incorrect!"
    assert dot_product.matrix == (sample1 @ sample2).tolist(), "Dot product of matrices is incorrect!"

    save_matrix_to_txt(addition, f"{txt_save_path}/matrix+.txt")
    save_matrix_to_txt(point_wise_multiplication, f"{txt_save_path}/matrix*.txt")
    save_matrix_to_txt(dot_product, f"{txt_save_path}/matrix@.txt")

