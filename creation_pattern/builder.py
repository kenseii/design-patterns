class Car:
    def __init__(self):
        self.__wheels = list()
        self.__engine = None
        self.__body = None

    def setBody(self, body):
        self.__body = body

    def attachWheel(self, wheel):
        self.__wheels.append(wheel)

    def setEngine(self, engine):
        self.__engine = engine

    def specification(self):
        print(f"body: {self.__body.shape}")
        print(f"engine horsepower: {self.__engine.horsepower}")
        print(f"tire size: {self.__wheels[0].size}")


# ==== Car parts ===
class Wheel:
    size = None


class Engine:
    horsepower = None


class Body:
    shape = None


class Director:
    __builder = None

    def setBuilder(self, builder):
        self.__builder = builder

    # the algorithm for assembling a car
    def getCar(self):
        car = Car()

        # First goes the body
        body = self.__builder.getBody()
        car.setBody(body)

        # then the engine
        engine = self.__builder.getEngine()
        car.setEngine(engine)

        # then 4 wheels
        i = 0
        while i < 4:
            wheel = self.__builder.getWheel()
            car.attachWheel(wheel)
            i += 1

        return car


class BuilderInterface:
    def getWheel(self): pass

    def getEngine(self): pass

    def getBody(self): pass


# one implementation
class JeepBuilder(BuilderInterface):
    def getWheel(self):
        wheel = Wheel()
        wheel.size = 22
        return wheel

    def getEngine(self):
        engine = Engine()
        engine.horsepower = 400
        return engine

    def getBody(self):
        body = Body()
        body.shape = "SUV"
        return body


class NissanBuilder(BuilderInterface):
    def getWheel(self):
        wheel = Wheel()
        wheel.size = 16
        return wheel

    def getEngine(self):
        engine = Engine()
        engine.horsepower = 100
        return engine

    def getBody(self):
        body = Body()
        body.shape = "hatchback"
        return body


if __name__ == "__main__":
    d = Director()
    # lets build a jeep
    d.setBuilder(JeepBuilder())
    # check the returned object
    print(d.getCar())
    # check the car's specs
    print(d.getCar().specification())

    # lets build a Nissan with the same director
    d.setBuilder(NissanBuilder())
    # check the returned object
    print(d.getCar())
    # check the car's specs
    print(d.getCar().specification())
