# ==== abstract shape classes ====
class Shape2DInterface:
    def draw(self): pass


class Shape3DInterface:
    def build(self): pass


# ==== concrete shape classes ====
class Circle(Shape2DInterface):
    def draw(self):
        print("Circle.draw")


class Square(Shape2DInterface):
    def draw(self):
        print("Square.draw")


class Sphere(Shape3DInterface):
    def build(self):
        print("Sphere.build")


class Cube(Shape3DInterface):
    def build(self):
        print("Cube.build")


# ==== Abstract shape factory ===
class ShapeFactoryInterface:
    @staticmethod
    def getShape(sides): pass


# ==== Concrete shape factories ===
# the ones supposed to be used outside
class Shape2DFactory(ShapeFactoryInterface):
    @staticmethod
    def getShape(sides):
        if sides == 1:
            return Circle()
        if sides == 4:
            return Square()
        assert 0, f"2D shape not defined for {sides} sides"


class Shape3DFactory(ShapeFactoryInterface):
    @staticmethod
    def getShape(sides):
        """sides mean faces here"""
        if sides == 1:
            return Sphere()
        if sides == 6:
            return Cube()
        assert 0, f"3D shape not defined for {sides} sided/faces"


if __name__ == "__main__":
    s2 = Shape2DFactory()
    print(s2.getShape(1))
    s2.getShape(1).draw()
    # 3D
    s3 = Shape3DFactory()
    print(s3.getShape(1))
    s3.getShape(1).build()
