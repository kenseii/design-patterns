class SubjectInterface:
    """
    Define the common interface for the realsubject and proxy so that a
    proxy can be used anywhere a realsubject is expected
    """

    def request(self): pass


class Proxy(SubjectInterface):
    """
    Maintain a reference that lets the proxy access the real subject.
    Provide an interface identical to Subject's
    """

    def __init__(self, real_subject):
        self._real_subject = real_subject

    def request(self):
        print("Proxy may be doing something, like controlling access")
        self._real_subject.request()


class RealSubject(SubjectInterface):
    """
    Define the real object that the proxy represents.
    """

    def request(self):
        print("The real object is dealing with the request")


if __name__ == "__main__":
    rs = RealSubject()
    # accessing the real object directly
    rs.request()
    proxy = Proxy(rs)
    # accessing the object through the proxy
    proxy.request()
