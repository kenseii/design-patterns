# Adaptee (source) interface
class EuropeanSocketInterface:
    def voltage(self): pass

    def live(self): pass

    def neutral(self): pass

    def earth(self): pass


# target interface
class USASocketInterface:
    def voltage(self): pass

    def live(self): pass

    def neutral(self): pass


# Adaptee
class EuropeanSocket(EuropeanSocketInterface):
    def voltage(self):
        return 230

    def live(self):
        return 1

    def neutral(self):
        return -1

    def earth(self):
        return 0


# client
class AmericanKettle:
    __power = None

    def __init__(self, power):
        self.__power = power

    def boil(self):
        if self.__power.voltage() > 110:
            print("Kettle on fire")
        else:
            if self.__power.live() == 1 and self.__power.neutral() == -1:
                print("Coffee time")
            else:
                print("No power")


# defining the adapter to make the kettle work on european
# passing in the target
class Adapter(USASocketInterface):
    __socket = None

    def __init__(self, socket):
        self.__socket = socket

    def voltage(self):
        return 110

    def live(self):
        return self.__socket.live()

    def neutral(self):
        return self.__socket.neutral()


if __name__ == "__main__":
    socket = EuropeanSocket()
    # attempt to use the american kettle on 230v, Not a good idea
    kettle = AmericanKettle(socket)
    kettle.boil()
    # now trying with an adapter
    adapter = Adapter(socket)
    kettle = AmericanKettle(adapter)
    kettle.boil()
