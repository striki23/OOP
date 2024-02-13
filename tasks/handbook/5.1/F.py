class Rectangle:

    def __init__(self, point_A, point_B):
        self.point_A = point_A
        self.point_B = point_B
        self.side_1 = abs(point_B[0] - point_A[0])
        self.side_2 = abs(point_B[1] - point_A[1])

    def perimeter(self):
        return round(((self.side_1 + self.side_2) * 2), 2)

    def area(self):
        return round((self.side_1 * self.side_2), 2)

    def get_pos(self) -> tuple:
        return (
            min(self.point_A[0], self.point_B[0]),
            max(self.point_A[1], self.point_B[1])
        )

    def get_size(self) -> tuple:
        return round(self.side_1, 2), round(self.side_2, 2)

    def move(self, dx, dy):
        self.point_A = (
                round((self.point_A[0] + dx), 2),
                round((self.point_A[1] + dy), 2)
        )
        self.point_B = (
            round((self.point_B[0] + dx), 2),
            round((self.point_B[1] + dy), 2)
        )
    # не получилось оптимизировать код.. из-за self

    def resize(self, width, height):
        self.side_1 = width
        self.side_2 = height
        self.point_A = self.get_pos()
        self.point_B = (
            (self.point_A[0] + width),
            (self.point_A[1] - height)
        )


rect = Rectangle((7.52, -4.3), (3.2, 3.14))
print(rect.get_pos(), rect.get_size())
rect.resize(23.5, 11.3)
print(rect.get_pos(), rect.get_size())


