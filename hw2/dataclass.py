from enum import Enum


class LatexTable(Enum):
    Space: str = " "
    LineEnd: str = r'\\'
    OpenBrace: str = "{"
    CloseBrace: str = "}"
    ColumnDividerSymbol: str = "|"
    ColumnDivider: str = "c|"
    InnerColumnDivider: str = "&"
    StraightLine: str = "\hline"
    StartTable: str = r'\documentclass{article} \usepackage[utf8]{inputenc} \begin{tabular}'
    EndTable: str = '\end{tabular} \end{document}'
