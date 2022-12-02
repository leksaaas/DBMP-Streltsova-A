import math
import numbers


class CNumbers:

    def __init__(self, xpart = 0, ypart = 0):
        self.set(xpart, ypart)

    def set(self, xpart, ypart):
        if isinstance(xpart, numbers.Number) and isinstance(ypart, numbers.Number):
           self.a = xpart
           self.b = ypart
        else:
           raise ValueError

    def get(self, exp = False):
        if exp == True:
            return self.r, self.f
        else:
            return self.a, self.b




    def perevodchikvexp(self):
        if self.a==0:
            raise Exception("Перевод невозможен")
        self.r = math.sqrt(self.a**2 + self.b**2)
        if self.a < 0 and self.b > 0:
            self.f = math.pi - math.atan(abs(self.b) / abs(self.a))
        elif self.a < 0 and self.b < 0:
            self.f = math.pi + math.atan(abs(self.b) / abs(self.a))
        elif self.a > 0 and self.b < 0:
            self.f = - math.atan(self.b/self.a)
        else:
            self.f = math.atan(self.b / self.a)

        return self.r, self.f

    def perevodchikvalg(self):
        self.r = self.a
        self.f = self.b
        self.x = self.r * math.cos(self.f)
        self.y = self.x * math.tan(self.f)

        return self.x, self.y

    def __add__(self, other):
        if isinstance(other, numbers.Number):
            return self.a + other, self.b
        else:
            return self.a + other.a, self.b + other.b

    def __radd__(self, other):
        if isinstance(other, numbers.Number):
            return self.a + other, self.b
        else:
            return self.a + other.a, self.b + other.b

    def __sub__(self, other):
        if isinstance(other, numbers.Number):
            return self.a - other, self.b
        else:
            return self.a - other.a, self.b - other.b

    def __rsub__(self, other):
        if isinstance(other, numbers.Number):
            return other - self.a, self.b
        else:
            return other.a - self.a, other.b - self.b

    def __mul__(self, other):
        if isinstance(other, numbers.Number):
            return self.a * other, self.b * other
        else:
            return self.a * other.a - self.b * other.b, self.a * other.b + self.b * other.a

    def __rmul__(self, other):
        if isinstance(other, numbers.Number):
            return self.a * other, self.b * other
        else:
            return other.a * self.a - other.b * self.b, other.a * self.b + other.b * self.a

    def __floordiv__(self, other):
        if isinstance(other, numbers.Number):
            return round(self.a/other.a, 2), round(self.b/other.a, 2)
        else:
            return (self.a * other.a + self.b * other.b) / (other.a ** 2 + other.b ** 2), (self.b * other.a - self.a * other.b) / (other.a ** 2 + other.b ** 2)

    def __rfloordiv__(self, other):
        if isinstance(other, numbers.Number):
            return round(other/self.a, 2), round(other/self.b, 2)
        else:
            return (other.a * self.a + other.b * self.b) / (self.a ** 2 + self.b ** 2), (other.b * self.a - other.a * self.b) / (self.a ** 2 + self.b ** 2)

    def __str__(self, exp = False):
            return str(self.a) + "+i*" + str(self.b) + '   '+ str(self.perevodchikvexp()[0]) + '*exp^(i*' + str(self.perevodchikvexp()[1]) + ")"

    def __eq__(self, other):
        if isinstance(other, numbers.Number):
            return (self.a == other and self.b == 0)
        else:
            return self.a == other.a and self.b == other.b

    def __abs__(self):
        return math.sqrt(self.a**2 + self.b**2)

    def __getitem__(self, key):
        if key == 0:
            return self.a
        elif key == 1:
            return self.b
        else:
            raise ValueError

    def __setitem__(self, key, value):
        if key == 0:
            self.a = value
        elif key == 1:
            self.b = value
        else:
            raise ValueError
print('Введите ваши числа: 1-ое число - действительная часть 1-го, 2-ое - его мнимая часть, 3-е - действительная часть 2-го, 4-е - его мнимая часть')
try:
    a=[float(k) for k in input().split()]
except ValueError:
    print('Вы ввели что-то не то')
else:
    try:
        A=CNumbers(a[0],a[1])
        B=CNumbers(a[2],a[3])
    except IndexError:
        print('Введите 4 числа')
print('Выберите действие: +,-,/,*,perevodvexp,abs')
d=input()
try:
    if d not in ('+','-','/','*','perevosvexp','abs'):
        raise TypeError
except TypeError:
    print('Я такое не умею')
if d=='+':
    print(A+B)
elif d=='-':
    print(A-B)
elif d=='/':
    try:
      print(A/B)
    except ZeroDivisionError:
        print('Нельзя делить на 0')
elif d=='*':
    print(A*B)
elif d=='perevodvexp':
    try:
        print('A=',A.perevodchikvexp())
    except Exception:
        print('Перевод первого числа невозможен')
    try:
        print('B=',B.perevodchikvexp())
    except Exception:
        print('Перевод второго числа невозможен')
elif d=='abs':
    print('abs(A)=',abs(A))
    print('abs(B)=', abs(B))
