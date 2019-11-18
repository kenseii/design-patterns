class Singleton:
    __instance = None

    def __new__(cls, val=None):
        if Singleton.__instance is None:
            Singleton.__instance = object.__new__(cls)
        Singleton.__instance.val = val
        return Singleton.__instance


if __name__ == "__main__":
    x = Singleton()
    x.val = "burger"
    print(x.val)

    # lets attempt to create another instance
    y = Singleton()
    y.val = "chips"
    print(y.val)

    print(y == x)
