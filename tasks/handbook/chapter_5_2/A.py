class Point:
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def move(self, a, b):
        self.x += a
        self.y += b

    def length(self, point):
        return round(abs(((
                     self.x - point.x) ** 2 + (
                     self.y - point.y) ** 2) ** 0.5), 2
                    )


class PatchedPoint(Point):
    def __init__(self,
                 x: int | tuple[int, int] = 0,
                 y: int = 0) -> None:
        if isinstance(x, tuple):
            x, y = x
        super().__init__(x=x, y=y)


if __name__ == '__main__':
    first_point = PatchedPoint((2, -7))
    second_point = PatchedPoint(7, 9)
    print(first_point.length(second_point))
    print(second_point.length(first_point))
