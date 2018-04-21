from math import gcd


def unused_gcd(a, b):
    # Just to prove thath i can implement that function, but for permormance
    # reasons i choose to use the already existent `math.gcd`
    remainder = a % b
    return b if remainder == 0 else unused_gcd(b, remainder)


class Term:
    def __init__(self, numerator, denominator=1):
        if denominator == 0:
            raise ZeroDivisionError('"denominator" should not be zero')

        if isinstance(numerator, Term) and denominator == 1:
            self.numerator = numerator.numerator
            self.denominator = numerator.denominator

        elif isinstance(numerator, int) and isinstance(denominator, int):
            # if both are just integers
            self.numerator = numerator
            self.denominator = denominator

        else:
            _numerator = to_integer_ratio(numerator)
            _denominator = to_integer_ratio(denominator)
            temp = Term(*(_numerator)) / Term(*(_denominator))
            self.numerator = temp.numerator
            self.denominator = temp.denominator
        self.simplify()

#        if isinstance(numerator, int) and isinstance(denominator, int):
#            # if both are just integers
#            self.numerator = numerator
#            self.denominator = denominator
#        else:
#            # one of them is float or Term
#            numerator = (float(numerator) if isinstance(numerator, int)
#                         else numerator)
#            denominator = (float(denominator) if isinstance(denominator, int)
#                           else denominator)
#
#            numerator = Term(*(numerator.as_integer_ratio()))
#            denominator = Term(*(denominator.as_integer_ratio()))
#            result = numerator / denominator
#            self.numerator = result.numerator
#            self.denominator = result.denominator
#        self.simplify()

    def __repr__(self):
        return (f'Term({self.numerator})' if self.denominator == 1
                else f'Term({self.numerator}, {self.denominator})')

    def __str__(self):
        return (f'{self.numerator}' if self.denominator == 1
                else f'{self.numerator}/{self.denominator}')

    def __mul__(self, other):
        if isinstance(other, Term):
            return Term(self.numerator * other.numerator,
                        self.denominator * other.denominator)
        else:
            return self * Term(other)

    def __div__(self, other):
        return self.__truediv__(other)

    def __truediv__(self, other):
        if isinstance(other, Term):
            return Term(self.numerator * other.denominator,
                        self.denominator * other.numerator)
        else:
            return self / Term(other)

    def __add__(self, other):
        if isinstance(other, Term):
            return Term(
                (self.numerator * other.denominator +
                 self.denominator * other.numerator),
                self.denominator * other.denominator
            )
        else:
            return self + Term(other)

    def __sub__(self, other):
        if isinstance(other, Term):
            return Term(
                (self.numerator * other.denominator -
                 self.denominator * other.numerator),
                self.denominator * other.denominator
            )
        else:
            return self - Term(other)

    # def __deepcopy__(self):
    #     return Term(self.numerator, self.denominator)

    def __eq__(self, other):
        if isinstance(other, Term):
            self.simplify()
            other.simplify()
            return (self.numerator == other.numerator and
                    self.denominator == other.denominator)
        else:
            return self == Term(other)

    def __float__(self):
        return float(self.numerator / self.denominator)

    def __bool__(self):
        return not self.is_zero()

    def simplify(self):
        _gcd = gcd(self.numerator, self.denominator)
        self.numerator = self.numerator // _gcd
        self.denominator = self.denominator // _gcd

    def as_integer_ratio(self):
        self.simplify()
        return (self.numerator, self.denominator)

    def is_zero(self):
        return self.numerator == 0 or float(self) == 0


def to_integer_ratio(n: [int, float, Term]) -> (int, int):
    if isinstance(n, int):
        return (n, 1)
    elif isinstance(n, Term):
        return n.as_integer_ratio()
    elif isinstance(n, float):

        if n.is_integer():
            return (int(n), 1)
        else:
            strnum = str(n).split('.')
            return (int(strnum[0] + strnum[1]), 10 ** len(strnum[1]))