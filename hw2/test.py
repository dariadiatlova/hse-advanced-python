import pytest
from hw2.generate_latex_table import create_latex_table


def test_latex_table(sequence):
    """
    Test checks that the function creates expected expression for a couple of samples.
    """
    key, value = sequence
    if value != AssertionError:
        assert value == create_latex_table(key)
    else:
        try:
            create_latex_table(key)
            raise AssertionError(f"Function supposed to raise Assertion Error with following input: {key}")
        except AssertionError:
            pass


@pytest.fixture(params=[([["id", "name", "age"], [0, "Cody", "29"], [1, "Sarah", "26"], [2, "Mike", "57"]],
                         r"\documentclass{article} \usepackage[utf8]{inputenc} \usepackage{graphicx} \begin{document} "
                         r"\begin{tabular}{|c|c|c|} \hline id&name&age\\ \hline 0&Cody&29\\ \hline 1&Sarah&26\\ "
                         r"\hline 2&Mike&57\\ \hline \end{tabular} \end{document}"),

                        ([[1, 2, 3], [1, 2], [1, 2, 3]], AssertionError)])
def sequence(request):
    """
    Consistently yields 2 tuples: list of lists to create table and str to create latex table).
    """
    yield request.param
