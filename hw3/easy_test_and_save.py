import numpy as np
from hw3 import HW3_ROOT_PATH
from hw3.matrix_library import Matrix
np.random.seed(0)


def test_easy_task(txt_save_path: str = f"{HW3_ROOT_PATH}/artifacts"):
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

    with open(f"{txt_save_path}/matrix+.txt", "w") as f:
        f.write(addition.__str__())

    with open(f"{txt_save_path}/matrix*.txt", "w") as f:
        f.write(point_wise_multiplication.__str__())

    with open(f"{txt_save_path}/matrix@.txt", "w") as f:
        f.write(dot_product.__str__())
