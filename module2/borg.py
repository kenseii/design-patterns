class Borg:
    __shared_state = {}

    def __init__(self):
        self.__dict__ = self.__shared_state


# all the instances are different but will share the same state


if __name__ == "__main__":
    b = Borg()
    c = Borg()
    # not same
    print(b == c)
    # but same state
    b.val = "みんな同じ"
    # as shown here
    print(c.val)
