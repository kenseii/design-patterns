class Engine:
    def __init__(self):
        # how much the motor is spinning in rpm
        self.spin = 0

    def start(self, spin):
        self.spin = min(spin, 3000)


class StarterMotor:

    def __init__(self):
        # how much the motor is spinning in rpm
        self.spin = 0

    def start(self, charge):
        if charge > 50:
            # if there is enough power spin fast
            self.spin = 2500


class Battery:

    def __init__(self):
        # % charged, starts flat
        self.charge = 0


class Car:
    # the facade object that deals with the battery, engine, starter motor
    def __init__(self):
        self.battery = Battery()
        self.starter = StarterMotor()
        self.engine = Engine()

    def turn_key(self):
        self.starter.start(self.battery.charge)
        self.engine.start(self.starter.spin)
        if self.engine.spin > 0:
            print("Engine started")
        else:
            print("Engine not started")

    def jump(self):
        self.battery.charge = 100
        print("Jumped")


if __name__ == "__main__":
    c = Car()
    # it wont start
    c.turn_key()
    # igikurikiyeho nugushitura :-)
    c.jump()
    # it will start now
    c.turn_key()
