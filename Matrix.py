def zipWith(one, two):
    assert(len(two) == len(one))
    a = 0
    for i in range(len(one)):
       a += one[i] * two[i]
    return a

class LinearSpace():
    def __radd__(self, other):
        return self + other

    def __iadd__(self, other):
        return self + other

    def __sub__(self, other):
        return self + (-1)*other

    def __rsub__(self, other):
       return other - self

    def __truediv(self, other):
        assert(isinstance(other, type(1)) or isinstance(other, type(0.1)))
        return self * (other ** (-1))

class Matrix(LinearSpace):
    def __init__(self, m, n = None):
        if isinstance(n, type(None)):
            self.matrix = m
        else:
            condition = isinstance(m, type(1)) and isinstance(n, type(1))
            assert (condition)
            self.matrix = [[None for j in range(n)] for i in  range(m)]

    def output(self):
        for i in range(self.get_m()):
            print (self.get_line(i))


    def get_m(self):
        return len(self.matrix)

    def get_n(self):
        return len(self.matrix[0])

    def get_size(self):
        return (self.get_n(), self.get_m())

    def get(self, i, j):
        return self.matrix[i][j]

    def get_line(self, i):
        return self.matrix[i]

    def get_colum(self, j):
        colum = [self.get(i, j) for i in range(self.get_m())]
        return colum

    def set(self, i, j, value):
        self.matrix[i][j] = value

    def __eq__(self, other):
        assert(isinstance(other, type(self)))
        assert(self.get_size() == other.get_size())
        for i in range(self.get_m()):
            for j in range(self.get_n()):
                if self.get(i, j) != other.get(i, j):
                    return False
        return True

    def __add__(self, other):
        assert(isinstance(other, type(self)))
        assert(self.get_size() == other.get_size)
        m = self.get_m()
        n = self.get_n()
        matrix = [[self.get(i, j) + other.get(i, j) for j in range(n)] for i in range(m)]
        return Matrix(matrix)

    def __mul__(self, other):
        if isinstance(other, type(1)) or isinstance(other, type(0.1)):
           matrix = [[other * self.get(i, j) for j in range(self.get_n())] for i in range(self.get_m())]
           return Matrix(matrix)
        elif isinstance(other, type(self)):
            m = self.get_m()
            k = other.get_n()
            matrix = [[zipWith(self.get_line(i), other.get_colum(j)) for j in range(k)] for i in range(m)]
            return Matrix(matrix)

    def minor(self, x, y):
        minor = [[self.get(i,j) for j in range(self.get_n()) if j != y] for i in range(self.get_m()) if i != x]
        return Matrix(minor)

    def determinant(self):
        assert (self.get_m() == self.get_n())
        if self.get_size() == (1, 1):
           return self.get(0, 0)
        else:
          answer = 0
          for i in range(self.get_m()):
              minor = self.minor(0, i)
              answer += ((-1) ** i) * minor.determinant()
          return answer

    def algebraicaddition(self, i, j):
        minor = self.minor(i, j)
        return (-1 ** (i + j)) * minor.determinant()

    def transpose(self):
        matrix = [[self.get(i, j) for i in range(self.get_m())] for j in range(self.get_n())]
        return Matrix(matrix)

    def invert(self):
        allymatrix = [[self.algebraicaddition(i, j) for j in range(self.get_n())] for i in range(self.get_m())]
        return allymatrix / self.determinant()

def tests():
    one = Matrix([[1, 0], [0, 1]])
    two = Matrix([[1,2], [3,4]])
    three = one * two
    three.output()

tests()
