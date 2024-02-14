class Rectangle:

    def __init__(self, point_a, point_b):
        self.point_a = point_a
        self.point_b = point_b
        self.side_1, self.side_2 = self.__set_sides()

    def perimeter(self):
        return round(((self.side_1 + self.side_2) * 2), 2)

    def area(self):
        return round((self.side_1 * self.side_2), 2)

    def __set_sides(self) -> tuple[float, float]:
        x_1, y_1 = self.point_a
        x_2, y_2 = self.point_b

        return abs(x_2 - x_1), abs(y_2 - y_1)
