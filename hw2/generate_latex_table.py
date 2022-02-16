from typing import Union, NoReturn, Optional

from hw2 import HW_2_ROOT_PATH
from hw2.dataclass import LatexTable


def sanity_check(data: list[list[Union[int, str, float]]], columns_number: int) -> NoReturn:
    """
    Function takes the list and checks that it can be converted into rectangular table, raise an error otherwise.
    :param data: List of list
    :param columns_number: int, expected number of values in each list.
    :return: NoReturn
    """
    for row in data:
        assert len(row) == columns_number, "All rows should have the same number of elements."


def get_start_for_table(columns_count: int) -> str:
    """
    Function takes an integer number of columns to create and returns a construction:
    "\begin{tabular}{|c|c|c|c|} \hline", where number of c's is equal to the amount of columns in a table.
    :param columns_count: int, number of columns in a table
    :return: str, described as in docstring above.
    """
    inner_column_series = LatexTable.ColumnDivider.value * columns_count
    return (LatexTable.StartTable.value + LatexTable.OpenBrace.value + LatexTable.ColumnDividerSymbol.value +
            inner_column_series + LatexTable.CloseBrace.value + LatexTable.Space.value + LatexTable.StraightLine.value
            + LatexTable.Space.value)


def get_row_for_table(row: list[Union[int, str, float]]) -> str:
    """
    Function takes a row represented as a list with n values for n columns. If row = [1, 2, 3, 4],
    then returns '1 & 2 & 3 & 4\\'.
    :param row: list of values to write to the table
    :return: str, described as in docstring above.
    """
    return (LatexTable.InnerColumnDivider.value.join(map(str, row)) + LatexTable.LineEnd.value +
            LatexTable.Space.value + LatexTable.StraightLine.value + LatexTable.Space.value)


def get_end_for_table():
    """
    Function does not take any arguments and returns the srting to finish latex table: '\end{tabular}'.
    :return:
    """
    return LatexTable.EndTable.value


def create_latex_table(data_to_create_table: list[list[Union[str, float, int]]],
                       tex_file_save_path: Optional[str] = None):

    columns_number = len(data_to_create_table[0])
    rows_number = len(data_to_create_table)
    sanity_check(data_to_create_table, columns_number)
    inner_table_data = "".join(map(str, [get_row_for_table(data_to_create_table[i]) for i in range(rows_number)]))
    latex_row = get_start_for_table(columns_number) + inner_table_data + get_end_for_table()

    if tex_file_save_path:
        with open(tex_file_save_path, 'w') as f:
            f.write(latex_row)

    return latex_row


if __name__ == "__main__":
    create_latex_table([["id", "name", "age"], [0, "Cody", "29"], [1, "Sarah", "26"], [2, "Mike", "57"]],
                       f"{HW_2_ROOT_PATH}/artifacts/table.tex")
