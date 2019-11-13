class Pet(object):
    """Base class for all pets"""
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def getName(self):
        return self.name

    def getSpecies(self):
        return self.species

    def __str__(self):
        return "%s is a %s" % (self.name, self.species)


class Dog(Pet):

    def __init__(self, name, chases_cats):
        super().__init__(name, "Dog")
        self.chases_cats = chases_cats

    def chasesCats(self):
        return self.chases_cats

    def __str__(self):
        additional_info = ""
        if self.chases_cats:
            additional_info = " who chases cats"
        # this adds the extra text on the return
        # TODO you didnt know that so oboenasai...
        return super().__str__() + additional_info


if __name__ == "__main__":
    p = Pet('eric', 'parrot')
    print(p)
    print(Pet.__subclasses__())

    d = Dog("Ignace", True)
    print(d)
    print(Dog.__bases__)