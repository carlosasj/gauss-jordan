from .line import Line
from .aux_functions import find_pivot, file_to_matrix
from typing import List


def do_gauss_jordan(matrix: List[Line]):
    LEN_MATRIX = len(matrix)

    for i in range(LEN_MATRIX):
        pivot_line = find_pivot(matrix, i)
        if find_pivot != i:
            # swap lines
            matrix[i], matrix[pivot_line] = matrix[pivot_line], matrix[i]

        for j in range(i + 1, LEN_MATRIX):
            multiplier = matrix[j][i] / matrix[i][i]
            matrix[j] = matrix[j] - matrix[i] * multiplier

    for i in range(LEN_MATRIX - 1, -1, -1):
        # divide pivot to itself to make it equals 1
        matrix[i] = matrix[i] / matrix[i][i]

        for j in range(i):
            multiplier = matrix[j][i]
            matrix[j] = matrix[j] - matrix[i] * multiplier

    return matrix


def prompt():
    import argparse

    def fn_float(x):
        return float(x)

    def fn_fraction(x):
        return str(x)

    parser = argparse.ArgumentParser()
    parser.add_argument('--file', '-f', help='File to Read', required=True)
    parser.add_argument('--result-format', '-rf', help='Result Format',
                        default='fraction', choices=('fraction', 'float'))
    args = parser.parse_args()
    fn_format = fn_float if args.result_format == 'float' else fn_fraction

    matrix, terms_name = file_to_matrix(args.file)
    result = do_gauss_jordan(matrix)

    for i in range(len(terms_name)):
        print(f'{terms_name[i]} = {fn_format(result[i].augmented)}')


if __name__ == '__main__':
    prompt()
