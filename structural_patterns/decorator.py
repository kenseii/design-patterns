class WindowInterface:
    def build(self): pass


class AbstractWindowDecorator(WindowInterface):
    """
    Maintain a reference to a window object and define an interface
    that conforms to a window's interface.
    """

    def __init__(self, window):
        self._window = window

    def build(self): pass


class Window(WindowInterface):
    def build(self):
        print("Building window")


# =============== Concrete implementations =====================
class BorderDecorator(AbstractWindowDecorator):
    def add_border(self):
        print("Adding border")

    def build(self):
        self.add_border()
        self._window.build()


class VerticalSBDecorator(AbstractWindowDecorator):
    def add_vertical_scroll_bar(self):
        print("Adding vertical scroll bar")

    def build(self):
        self.add_vertical_scroll_bar()
        self._window.build()


class HorizontalSBDecorator(AbstractWindowDecorator):
    def add_horizontal_scroll_bar(self):
        print("Adding horizontal scroll bar")

    def build(self):
        self.add_horizontal_scroll_bar()
        self._window.build()


if __name__ == "__main__":
    w = Window()
    w.build()
    print("==============")
    # this will add a border before building the window
    wb = BorderDecorator(w)
    wb.build()
    print("==============")
    # add border and vertical scroll bar
    wbv = VerticalSBDecorator(wb)
    wbv.build()
    print("==============")
    # now we add everything
    best_window = HorizontalSBDecorator(wbv)
    best_window.build()
