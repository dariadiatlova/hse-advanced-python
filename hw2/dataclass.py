from enum import Enum


class LatexStrings(Enum):
    Space: str = " "
    LineEnd: str = r'\\'
    OpenBrace: str = "{"
    CloseBrace: str = "}"
    ColumnDividerSymbol: str = "|"
    ColumnDivider: str = "c|"
    InnerColumnDivider: str = "&"
    StraightLine: str = r'\hline'
    StartTable: str = r'\documentclass{article} \usepackage[utf8]{inputenc} \usepackage{graphicx} \begin{document} ' \
                      r'\begin{tabular}'
    EndTable: str = r'\end{tabular}'
    EndDocument: str = r'\end{document}'
    StartImage: str = r"\begin{figure} \includegraphics[width=\linewidth]{"
    EndImage: str = r"}\end{figure}"
