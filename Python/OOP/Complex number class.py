class ComplexNumbers:
    def __init__(self, r, i):
        self.Real = r
        self.Imag = i

    def plus(self, c2):
        self.Real = self.Real + c2.Real
        self.Imag = self.Imag + c2.Imag

    def multiply(self, c2):
        real = self.Real
        imag = self.Imag
        self.Real = real * c2.Real - imag * c2.Imag
        self.Imag = real * c2.Imag + c2.Real * imag

    def Print(self):
        print(self.Real, " + i", self.Imag, sep="")


r1, i1 = map(int, input().split())
r2, i2 = map(int, input().split())
choice = int(input())
c1 = ComplexNumbers(r1, i1)
c2 = ComplexNumbers(r2, i2)

if choice == 1:
    c1.plus(c2)
    c1.Print()
elif choice == 2:
    c1.multiply(c2)
    c1.Print()
else:
    print()
