class Cell:
    def __init__(self, sub_cells):
        self.sub_cells = sub_cells

    def __add__(self, other):
        return self.sub_cells + other.sub_cells

    def __sub__(self, other):

        pass

    def __mul__(self, other):
        pass

    def __truediv__(self, other):
        pass
