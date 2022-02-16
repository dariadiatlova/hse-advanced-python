from enum import Enum


class LatexTable(Enum):
    Space: str = " "
    LineEnd: str = r'\\'
    OpenBrace: str = "{"
    CloseBrace: str = "}"
    ColumnDividerSymbol: str = "|"
    ColumnDivider: str = "c|"
    InnerColumnDivider: str = "&"
    StraightLine: str = r'\hline'
    StartTable: str = r'\documentclass{article} \usepackage[utf8]{inputenc} \begin{document} \\usepackage{graphicx} ' \
                      r'\begin{tabular}'
    EndTable: str = r'\end{tabular} \end{document}'

