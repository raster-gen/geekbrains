class Cell:
    def __init__(self, sub_cells, cells_in_line):
        self.sub_cells = sub_cells
        self.cells_in_line = cells_in_line

    def __add__(self, other):
        return self.sub_cells + other.sub_cells

    def __sub__(self, other):
        if self.sub_cells > other.sub_cells:
            return self.sub_cells - other.sub_cells
        else:
            return 'Внимание: итоговое значение не положительное'

    def __mul__(self, other):
        return self.sub_cells * other.sub_cells

    def __floordiv__(self, other):
        return self.sub_cells // other.sub_cells

    @property
    def make_order(self):
        number_n = self.sub_cells // self.cells_in_line
        if number_n <= 0:
            return '*' * self.sub_cells
        else:
            lst = ['*'] * self.sub_cells
            for i in range(1, number_n + 1):
                lst.insert((self.cells_in_line * i) + (i-1), '\n')
        return ''.join(lst)


if __name__ == '__main__':
    # примеры
    cell_1 = Cell(21, 5)
    cell_2 = Cell(12, 3)
    print(cell_1.make_order)
    print()
    print(cell_2.make_order)
    print(cell_1 + cell_2)
    print(cell_1 - cell_2)
    print(cell_1 * cell_2)
    print(cell_1 // cell_2)
