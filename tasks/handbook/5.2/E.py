import math


class Fraction:

    def __init__(self, *args):
        self._args = args
        if len(self._args) == 2:
            self._num, self._denom = args[0], args[1]
        elif len(self._args) == 1:
            args = args[0].split('/')
            self._num, self._denom = int(args[0]), int(args[1])
        self._fraction_reduction()

    def _fraction_reduction(self):
        divisor = math.gcd(self._num, self._denom)
        self._num = self._num // divisor
        self._denom = self._denom // divisor

        if self._denom < 0:
            self._num = -self._num
            self._denom = abs(self._denom)

        return self

    def __str__(self):
        return f'{self._num}/{self._denom}'

    def __repr__(self):
        return f"Fraction('{self._num}/{self._denom}')"

    def __neg__(self):
        return Fraction(-self._num, self._denom)

    def numerator(self, number=None):
        if number is not None:
            if self._num < 0:
                self._num = -number
            else:
                self._num = number
            self._fraction_reduction()
        return abs(self._num)

    def denominator(self, number=None):
        if number is not None:
            self._denom = number
            self._fraction_reduction()
        return abs(self._denom)
