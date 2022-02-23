from hw3.matrix_library import Matrix


def save_matrix_to_txt(data: Matrix, file_path: str):
    with open(file_path, "w") as f:
        f.write(data.__str__())
