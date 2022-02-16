import subprocess

from typing import Union
from hw1_package.ast import main

from hw2.dataclass import LatexStrings
from hw2 import HW_2_ROOT_PATH
from hw2.generate_latex_table import create_latex_table, write_tex


def save_fibonacci_picture(image_path: str = f"{HW_2_ROOT_PATH}/artifacts/ast.png") -> str:
    """
    Function takes path where ast image will be saved and returns the path to read the picture after that.
    :param image_path: str
    :return: str
    """
    main(image_path)
    return image_path


def get_picture_command() -> str:
    """
    Function runs ast image function and wraps it into LaTex syntax.
    :return: Latex string
    """
    return (LatexStrings.StartImage.value + f"{save_fibonacci_picture()}" + LatexStrings.EndImage.value
            + LatexStrings.Space.value)


def call_pdf_latex(tex_file_path: str) -> None:
    """
    Function calls pdflatex module to generate pdf into artifacts directory.
    :param tex_file_path: str
    :return: None
    """
    subprocess.call(['pdflatex', '-output-directory', f"{HW_2_ROOT_PATH}/artifacts/", tex_file_path], shell=False)


def run(data_to_create_table: list[list[Union[str, float, int]]], tex_file_path: str):
    """
    Function takes a list to create table and
    :param data_to_create_table:
    :param tex_file_path:
    :return:
    """
    latex_string = create_latex_table(data_to_create_table)
    end_of_document = LatexStrings.EndDocument.value
    latex_string_with_image = latex_string[:-len(end_of_document)] + get_picture_command() + end_of_document
    write_tex(latex_string_with_image, tex_file_path)
    call_pdf_latex(tex_file_path)


if __name__ == "__main__":
    run([["id", "name", "age"], [0, "Cody", "29"], [1, "Sarah", "26"], [2, "Mike", "57"]],
         f"{HW_2_ROOT_PATH}/artifacts/table_plus_image.tex")
