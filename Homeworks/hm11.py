class Point:
    def __init__(self, x, y):
        if isinstance(x, int | float) and isinstance(y, int | float):
            self.x_coord = x
            self.y_coord = y
        else:
            raise TypeError

    # def __str__(self):
    #     return f'Point {self.x_coord}:{self.y_coord}'


    def __add__(self, other):
        return Line(self, other)



class Line:
    def __init__(self, begin, end):
        if isinstance(begin, Point) or isinstance(end, Point):
            self.begin_point = begin
            self.end_point = end
        else:
            raise TypeError

    def __str__(self):
        return f'Line from [{self.begin_point}] to [{self.end_point}]'

    def length(self):
        k1 = self.begin_point.x_coord - self.end_point.x_coord
        k2 = self.begin_point.y_coord - self.end_point.y_coord

        return (k1 ** 2 + k2 ** 2) ** 0.5


class Triangle:
    def __init__(self,x, y, z):
        self.x_line = x
        self.y_line = y
        self.z_line = z

    def perimeter(self):
        x = self.x_line.length()
        y = self.y_line.length()
        z = self.z_line.length()
        return x + y + z

    def __str__(self):
        return f'ploshad = {self.perimeter}'

    def plosha(self):
        p = self.perimeter()
        res = (p*(p-self.x_line.length())*(p-self.y_line.length())*(p-self.z_line.length()))**0.5
        return res


p1 = Point(0, 3)
p2 = Point(4, 0)
p3 = Point(0, 0)


line1 = p1 + p2
line2 = p2 + p3
line3 = p3 + p1

print(line1.length())
print(line2.length())
print(line3.length())

treygolnik = Triangle(line1,line2,line3)
print(treygolnik.perimeter())
print(treygolnik.plosha())