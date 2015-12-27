import csv


class Vector:

    def __init__(self, x, y):
        self._x = x
        self._y = y

    @classmethod
    def from_list(cls, lst):
        return Vector(float(lst[0]), float(lst[1]))

    def minus(self, v):
        return Vector(self._x - v._x, self._y - v._y)

    def __repr__(self):
        return "Vector({},{})".format(self._x, self._y)

    @staticmethod
    def cross_product_mag(a, b):
        return b._y * a._x - b._x * a._y


class Triangle:

    def __init__(self, a, b, c):
        self._a = a
        self._b = b
        self._c = c

    @classmethod
    def from_coord_list(cls, coord_lst):
        return Triangle(
            Vector.from_list(coord_lst[0:2]),
            Vector.from_list(coord_lst[2:4]),
            Vector.from_list(coord_lst[4:6]))

    def __repr__(self):
        return "Triangle({},{},{})".format(self._a, self._b, self._c)

    def contains(self, p):
        prod_c = Vector.cross_product_mag(
            self._b.minus(self._a), p.minus(self._a))
        prod_a = Vector.cross_product_mag(
            self._c.minus(self._b), p.minus(self._b))
        prod_b = Vector.cross_product_mag(
            self._a.minus(self._c), p.minus(self._c))

        return ((prod_a < 0 and prod_b < 0 and prod_c < 0) or
                (prod_a > 0 and prod_b > 0 and prod_c > 0))


if __name__ == "__main__":

    origin = Vector(0, 0)
    with open("../data/p102_triangles.txt") as csvfile:
        triangle_reader = csv.reader(csvfile)
        print(sum(Triangle.from_coord_list(row).contains(origin)
                  for row in triangle_reader))
