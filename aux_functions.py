from line import Line
from typing import Iterable


def find_pivot(matrix, col: int) -> int:
    """
        Given the matrix and the column index,
        finds the line that should be swaped with the "current" pivot line.

        The number returned is the index of the line
    """

    col_terms = (matrix[line][col] for line in range(col, len(matrix)))
    col_terms_abs = list(map(abs, col_terms))
    max_abs = max(col_terms_abs)
    return col_terms_abs.index(max_abs) + col
