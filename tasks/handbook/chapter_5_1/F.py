class Rectangle:

    def __init__(self, point_a, point_b):
        self.point_a = point_a
        self.point_b = point_b
        self.side_1 = abs(point_b[0] - point_a[0])
        self.side_2 = abs(point_b[1] - point_a[1])

    def perimeter(self):
        return round(((self.side_1 + self.side_2) * 2), 2)

    def area(self):
        return round((self.side_1 * self.side_2), 2)

    def get_pos(self) -> tuple:
        return (
            min(self.point_a[0], self.point_b[0]),
            max(self.point_a[1], self.point_b[1])
        )

    def get_size(self) -> tuple:
        return round(self.side_1, 2), round(self.side_2, 2)

    def move(self, dx, dy):
        # TODO: Можно улучшить, вынести в отдельный метод.
        self.point_a = (
                round((self.point_a[0] + dx), 2),
                round((self.point_a[1] + dy), 2)
        )
        self.point_b = (
            round((self.point_b[0] + dx), 2),
            round((self.point_b[1] + dy), 2)
        )
    # не получилось оптимизировать код.. из-за self

    def resize(self, width, height):
        self.side_1 = width
        self.side_2 = height
        self.point_a = self.get_pos()
        self.point_b = (
            (self.point_a[0] + width),
            (self.point_a[1] - height)
        )

if __name__ == '__main__':
    rect = Rectangle((7.52, -4.3), (3.2, 3.14))
    print(rect.get_pos(), rect.get_size())
    rect.resize(23.5, 11.3)
    print(rect.get_pos(), rect.get_size())


