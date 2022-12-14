import math


class Fraction:
    def __init__(self, n, d):
        self.num = n
        self.den = d

    def add(self, n2):
        numerator = n1.num
        denominator = n1.den
        n1.num = numerator * n2.den + denominator * n2.num
        n1.den = denominator * n2.den

    def Mul(self, n2):
        n1.num *= n2.num
        n1.den *= n2.den

    def Gcd_and_Print(self):
        g = math.gcd(n1.num, n1.den)
        n1.num //= g
        n1.den //= g
        print("{}/{}".format(n1.num, n1.den))


num1, den1 = map(int, input().split())
q = int(input())
n1 = Fraction(num1, den1)
for i in range(q):
    c, num2, den2 = map(int, input().split())
    n2 = Fraction(num2, den2)
    if c == 1:
        n1.add(n2)
    elif c == 2:
        n1.Mul(n2)
    n1.Gcd_and_Print()
