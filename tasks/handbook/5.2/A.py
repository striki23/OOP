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


first_point = PatchedPoint((2, -7))
second_point = PatchedPoint(7, 9)
print(first_point.length(second_point))
print(second_point.length(first_point))