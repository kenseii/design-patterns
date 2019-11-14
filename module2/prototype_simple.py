from copy import deepcopy


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def move(self, x, y):
        self.x += x
        self.y += y

    def clone(self, move_x, move_y):
        """Creates a copy and move the coord somewhere in the plane"""
        obj = deepcopy(self)
        obj.move(move_x, move_y)

        return obj


if __name__ == "__main__":
    p0 = Point(0, 0)
    print(p0)
    p1 = p0.clone(1, 1)
    print(p1)
