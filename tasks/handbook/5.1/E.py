class Rectangle:

    def __init__(self, point_A, point_B):
        self.point_A = point_A
        self.point_B = point_B
        x_1, y_1 = point_A
        x_2, y_2 = point_B
        self.side_1 = abs(x_2 - x_1)
        self.side_2 = abs(y_2 - y_1)

    def perimeter(self):
        return round(((self.side_1 + self.side_2) * 2), 2)

    def area(self):
        return round((self.side_1 * self.side_2), 2)
