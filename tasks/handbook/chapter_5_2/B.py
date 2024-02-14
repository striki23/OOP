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
        return f'PatchedPoint{self}'

    def __str__(self):
        return f'({self.x}, {self.y})'


if __name__ == '__main__':
    point = PatchedPoint()
    print(point)
    point.move(2, -3)
    print(repr(point))
