import re
from .line import Line
from .term import Term
from typing import List, Iterable


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


def strip(s):
    return s.strip()


def to_term(x) -> Term:
    if '/' in x:
        tmp = Term(*list(map(float, x.split('/'))))
    elif '.' in x:
        tmp = float(x)
    else:
        tmp = int(x)

    return Term(tmp)


def iterable_to_matrix(lines: Iterable) -> (List[Line], List[str]):
    contents = re.compile(r'\[(.*?)\]')
    matrix: List[Line] = []
    terms_name: List[str] = []

    for line in lines:
            matched = contents.findall(line)
            line_terms = list(map(to_term, re.split(r', +', matched[0])))
            matrix.append(Line(line_terms, to_term(matched[2])))
            terms_name.append(matched[1])

    return matrix, terms_name


def file_to_matrix(filename: str) -> (List[Line], List[str]):
    matrix: List[Line] = []
    terms_name: List[str] = []
    with open(filename) as file:
        matrix, terms_name = iterable_to_matrix(file.readlines())

    return matrix, terms_name
