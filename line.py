from term import Term
from typing import Iterable, Union


class Line:
    def __init__(self, items: Iterable[Union[int, float, Term]],
                 augmented: Union[int, float, Term]):
        self.items = list(map(Term, items))
        self.augmented = Term(augmented)
        self.simplify()

    def simplify(self):
        map(lambda i: i.simplify(), self.items)
        self.augmented.simplify()

    def __repr__(self):
        return str(self)
        # return f"Line([{', '.join(map(repr, self.items))}], {repr(self.augmented)})"

    def __str__(self):
        cell = lambda i: '{:>8}'.format(str(i))
        return f"[{''.join(map(cell, self.items))}   |{cell(self.augmented)}  ]"

    def __mul__(self, other):
        if not isinstance(other, (int, float, Term)):
            raise NotImplementedError()

        term_other = Term(other)
        result_items = (i * term_other for i in self.items)
        result_augmented = self.augmented * term_other
        return Line(result_items, result_augmented)

    def __div__(self, other):
        return self.__truediv__(other)

    def __truediv__(self, other):
        if not isinstance(other, (int, float, Term)):
            raise NotImplementedError()

        term_other = Term(other)
        result_items = (i / term_other for i in self.items)
        result_augmented = self.augmented / term_other
        return Line(result_items, result_augmented)

    def __add__(self, other):
        if not isinstance(other, Line):
            raise NotImplementedError()
        result_items = map(sum, zip(self.items, other.items))
        result_augmented = self.augmented + other.augmented
        return Line(result_items, result_augmented)


    def __sub__(self, other):
        if not isinstance(other, Line):
            raise NotImplementedError()
        result_items = map(lambda x: x[0] - x[1], zip(self.items, other.items))
        result_augmented = self.augmented - other.augmented
        return Line(result_items, result_augmented)

    def __eq__(self, other):
        if not isinstance(other, Line):
            raise NotImplementedError()
        equal_items = all(map(lambda x: x[0] == x[1], zip(self.items, other.items)))
        if not equal_items:
            return False
        elif self.augmented == other.augmented:
            return True
        else:
            raise ValueError('Same items, different result')

    def __len__(self):
        return len(self.items)

    def __getitem__(self, key):
        if not isinstance(key, int):
            raise KeyError('Key must be an integer')
        return self.items[key]

    def __setitem__(self, key, value):
        if not isinstance(key, int):
            raise KeyError('Key must be an integer')
        self.items[key] = value

    def __delitem__(self, key):
        raise NotImplementedError()

    def __iter__(self):
        return iter(self.items)

    def __reversed__(self):
        return reversed(self.items)
