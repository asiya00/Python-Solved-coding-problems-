class Fraction:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        f1 = ((self.a * other.b) + (other.a * self.b))
        f2 = (self.b * other.b)
        return Fraction(f1, f2)

    def __sub__(self, other):
        f1 = ((self.a * other.b) - (other.a * self.b))
        f2 = (self.b * other.b)
        return Fraction(f1, f2)

    def __float__(self):
        return self.a/self.b

    def inverse(self):
        return Fraction(self.b, self.a)

    def __str__(self):
        return "{}/{}".format(self.a, self.b)


a = Fraction(1, 4)
b = Fraction(3, 4)
c = a + b
print(a)
print(c)
print(Fraction.__float__(c))
print(float(b.inverse()))
