from line import Line
from aux_functions import find_pivot
from pprint import pprint

LOG = False

matrix = [
    Line([2, -1,  3,  5],  -7),
    Line([6, -3, 12, 11],   4),
    Line([4, -1, 10,  8],   4),
    Line([0, -2, -8, 10], -60),
]

LEN_MATRIX = len(matrix)

for i in range(LEN_MATRIX):
    pivot_line = find_pivot(matrix, i)
    if find_pivot != i:
        # swap lines
        matrix[i], matrix[pivot_line] = matrix[pivot_line], matrix[i]

    for j in range(i + 1, LEN_MATRIX):
        multiplier = matrix[j][i] / matrix[i][i]
        matrix[j] = matrix[j] - matrix[i] * multiplier

        if LOG: print(f"\nL{j+1} <- L{j+1} - {multiplier}*L{i+1}")
        if LOG: pprint(matrix)

for i in range(LEN_MATRIX - 1, -1, -1):
    # divide pivot to itself to make it equals 1
    if LOG: print(f"\nL{i+1} <- L{i+1} / {matrix[i][i]}")
    matrix[i] = matrix[i] / matrix[i][i]

    if LOG: pprint(matrix)

    for j in range(i):
        multiplier = matrix[j][i]
        matrix[j] = matrix[j] - matrix[i] * multiplier

        if LOG: print(f"\nL{j+1} <- L{j+1} - {multiplier}*L{i+1}")
        if LOG: pprint(matrix)


print("\n\nResult:")
pprint(matrix)
# print(line.__repr__())
# print(line)

# sudo yum update; sudo yum install python36-devel; sudo pip-3.6 install ikp3db;