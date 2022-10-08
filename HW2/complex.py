import math
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
    def printing2(self):
        return print(self.r, '*e^(i',self.f,')' )
    def perevodchikvexp(self):
        self.r = math.sqrt(self.xpart ** 2 + self.ypart ** 2)
        if (self.xpart<0 and self.ypart <0) or (self.xpart<0 and self.ypart>0):
            self.f= math.pi +math.atan(self.ypart/self.xpart)
        elif self.xpart >0 and self.ypart<0:
            self.f=-math.atan(self.ypart/self.xpart)
        else:
            self.f = math.atan(self.ypart / self.xpart)
        return self.r,self.f
    def perevodcnikvalg(self):
        self.r=self.xpart
        self.f=self.ypart
        self.x=self.r*math.cos(self.f)
        self.y=self.x*math.tan(self.f)
        return self.x, self.y


def summator(self, other):
    return CNumbers(self.xpart + other.xpart, self.ypart + other.ypart)


def vichitator(self, other):
    return CNumbers(self.xpart - other.xpart, self.ypart - other.ypart)


def umnozhator(self, other):
    return CNumbers(self.xpart * other.xpart - self.ypart * other.ypart,
                    self.ypart * other.xpart + other.ypart * self.xpart)


def delitor(self, other):
    return CNumbers((self.xpart * other.xpart + self.ypart * other.ypart) / ((other.xpart) ** 2 + (other.ypart) ** 2),
                    (self.ypart * other.xpart - other.ypart * self.xpart) / ((other.xpart) ** 2 + (other.ypart) ** 2))


def sopryazhenie(self):
    return CNumbers(self.xpart, -self.ypart)


def modul(self):
    return print(math.sqrt(self.xpart ** 2 + self.ypart ** 2))




a = CNumbers(1, -1)
a.get()
a.printing()
b = CNumbers(1, 1)
z = delitor(a, b)
z.printing()
d = sopryazhenie(a)
d.printing()
modul(a)
a.perevodchikvexp()
a.printing2()
a.perevodcnikvalg()
a.printing()
p=umnozhator(a,b)
p.printing()