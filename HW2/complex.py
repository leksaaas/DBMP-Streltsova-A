class CNumbers:

    def __init__(self, xpart=0, ypart=0):
        self.set(xpart, ypart)

    def set(self, xpart, ypart):
        self.xpart = xpart
        self.ypart = ypart

    def get(self):
        return self.xpart, self.ypart

    def printing(self):
        return print(self.xpart, '+' if self.ypart >= 0 else '-', abs(self.ypart), 'i')


def summator(self, other):
    return CNumbers(self.xpart + other.xpart, self.ypart + other.ypart)


def vichitator(self, other):
    return CNumbers(self.xpart - other.xpart, self.ypart - other.ypart)


def umnozhator(self, other):
    return CNumbers(self.xpart * other.xpart - self.ypart * other.ypart,
                    self.ypart * other.xpart - other.ypart * self.xpart)


def delitor(self, other):
    return CNumbers((self.xpart * other.xpart + self.ypart * other.ypart) / ((other.xpart) ** 2 + (other.ypart) ** 2),
                    (self.ypart * other.xpart - other.ypart * self.xpart) / ((other.xpart) ** 2 + (other.ypart) ** 2))


def sopryazhenie(self):
    return CNumbers(self.xpart, -self.ypart)


def modul(self):
    return print((self.xpart ** 2 + self.ypart ** 2) ** (0.5))




a = CNumbers(1, -1)
a.get()
a.printing()
b = CNumbers(1, 1)
z = delitor(a, b)
z.printing()
d = sopryazhenie(a)
d.printing()
modul(a)