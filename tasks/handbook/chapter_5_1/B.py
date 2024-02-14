class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, a, b):
        self.x += a
        self.y += b

    def length(self, point: 'Point'):
        return round(abs(((
                    self.x - point.x) ** 2 + (
                    self.y - point.y) ** 2) ** 0.5), 2
                    )

