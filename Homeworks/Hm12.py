class Point:
    def __init__(self, x, y):
        if isinstance(x, int | float) and isinstance(y, int | float):
            self.x_coord = x
            self.y_coord = y
        else:
            raise TypeError

    def __str__(self):
        return f'Point {self.x_coord}:{self.y_coord}'


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
        self.vershiny = (x,y,z)


    @property
    def vershiny(self):
        return self._vershiny

    @vershiny.setter
    def vershiny(self,value):

        for i in value:
            if not isinstance(i, Point):
                raise TypeError
            else:
                print('checking accomplished')
                self._vershiny = value


    def plosha(self):
        line1 = self.vershiny[0] + self.vershiny[1]
        line2 = self.vershiny[1] + self.vershiny[2]
        line3 = self.vershiny[2] + self.vershiny[0]
        x = line1.length()
        y = line2.length()
        z = line3.length()

        p = (x+y+z)/2
        res = (p*(p-x)*(p-y)*(p-z))**0.5
        return res

    def __iter__(self):
        self.counter = -1
        return self

    def __next__(self):
        self.counter += 1
        if self.counter >= 3:
            raise StopIteration
        return self.vershiny[self.counter]



p1 = Point(0, 3)
p2 = Point(4, 0)
p3 = Point(0, 0)

treygolnik = Triangle(p1,p2,p3)

print(treygolnik.plosha())


for i in treygolnik:
    print(i)