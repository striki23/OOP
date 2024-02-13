class Point:

    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def move(self, a, b):
        self.x += a
        self.y += b

    def length(self, point):
        res = round(abs(((
                    self.x - point.x) ** 2 + (
                    self.y - point.y) ** 2) ** 0.5), 2
                    )
        return res


class PatchedPoint(Point):

    def __init__(self, *args):
        if not args:
            self.x = self.y = 0
        elif len(args) == 1 and isinstance(*args, tuple):
            args = args[0]
            self.x, self.y = args
        elif len(args) == 2:
            self.x, self.y = args

    def __repr__(self):
        return f'PatchedPoint{self.x, self.y}'

    def __str__(self):
        return f'{self.x, self.y}'

    def __add__(self, other_point):
        x, y = other_point
        other_point = PatchedPoint(self.x + x, self.y + y)
        return other_point

    def __iadd__(self, other_point):
        x, y = other_point
        self.x += x
        self.y += y
        return self


point = PatchedPoint()
print(point)
new_point = point + (2, -3)
print(point, new_point, point is new_point)
first_point = second_point = PatchedPoint((2, -7))
first_point += (7, 3)
print(first_point, second_point, first_point is second_point)
