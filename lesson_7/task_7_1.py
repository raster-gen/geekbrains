class Matrix:
    def __init__(self, lst):
        self.lst = lst

    def __str__(self):
        self.our_str = []
        for i in self.lst:
            for v in i:
                self.our_str.append(str(v))
                self.our_str.append('\t')
            self.our_str.append('\n')
        return ''.join(self.our_str)

    def __add__(self, other):
        # с проверкой на размер
        if len(self.lst) == len(other.lst):
            self.sum_matrix = [(k+v for k, v in zip(x, y)) for x, y in zip(self.lst, other.lst)]
            return Matrix(self.sum_matrix)
        else:
            print('Размер матриц разный')


if __name__ == '__main__':
    our_lst = [[2, 3, 5], [4, 5, 6], [6, 7, 7]]
    our_lst2 = [[5, 1, 7], [2, 4, 9], [0, 9, 1]]
    m = Matrix(our_lst)
    m2 = Matrix(our_lst2)
    print(m)
    print(m2)
    print(m + m2)
