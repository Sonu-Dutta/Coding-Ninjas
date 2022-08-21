from copy import deepcopy


class Polynomial:
    def __init__(self):
        self.capacity = 10
        self.degCoeff = [0]*10

    def __call__(self, p):
        degCoeff = p.defCoeff
        capacity = p.capacity

    def setCoefficient(self, degree, coeff):
        while(degree >= self.capacity):
            size = 2*self.capacity
            newDegCoeff = [0]*size
            for i in range(self.capacity):
                newDegCoeff[i] = self.degCoeff[i]
            self.capacity = size
            self.degCoeff = newDegCoeff

        self.degCoeff[degree] = coeff

    def print(self):
        for i in range(self.capacity):
            if(self.degCoeff[i] != 0):
                print(self.degCoeff[i], end="")
                print("x", end="")
                print(i, end=" ")
        print()

    def __add__(self, p):
        pNew = Polynomial()
        i, j = 0, 0
        while(i < self.capacity and j < p.capacity):
            deg = i
            coeff = self.degCoeff[i]+p.degCoeff[j]
            pNew.setCoefficient(deg, coeff)
            i, j = i+1, j+1
        while(i < self.capacity):
            pNew.setCoefficient(i, self.degCoeff[i])
            i += 1
        while(j < p.capacity):
            pNew.setCoefficient(j, p.degCoeff[j])
            j += 1
        return pNew

    def __sub__(self, p):
        pNew = Polynomial()
        i, j = 0, 0
        while(i < self.capacity and j < p.capacity):
            deg = i
            coeff = self.degCoeff[i]-p.degCoeff[j]
            pNew.setCoefficient(deg, coeff)
            i, j = i+1, j+1
        while(i < self.capacity):
            pNew.setCoefficient(i, self.degCoeff[i])
            i += 1
        while(j < p.capacity):
            pNew.setCoefficient(j, -p.degCoeff[j])
            j += 1
        return pNew

    def getCoefficient(self, degree):
        if (degree >= self.capacity):
            return 0
        return self.degCoeff[degree]

    def __mul__(self, p):
        pNew = Polynomial()
        for j in range(p.capacity):
            for i in range(self.capacity):
                deg = i + j
                coeff = pNew.getCoefficient(
                    deg) + (self.degCoeff[i] * p.degCoeff[j])
                pNew.setCoefficient(deg, coeff)
        return pNew


count1 = int(input())

degree1 = list(map(int, input().split()))

coeff1 = list(map(int, input().split()))


first = Polynomial()
for i in range(count1):
    first.setCoefficient(degree1[i], coeff1[i])

count2 = int(input())


degree2 = list(map(int, input().split()))

coeff2 = list(map(int, input().split()))


second = Polynomial()
for i in range(count2):
    second.setCoefficient(degree2[i], coeff2[i])


choice = int(input())

result = Polynomial()
# Add
if choice == 1:
    result = first + second
    result.print()
# Subtract
elif choice == 2:
    result = first - second
    result.print()
# Multiply
elif choice == 3:
    result = first * second
    result.print()

elif choice == 4:  # Copy constructor
    third = deepcopy(first)
    if (third.degCoeff == first.degCoeff):
        print("true")
    else:
        print("false")

else:  # Copy assignment operator
    fourth = deepcopy(first)
    if (fourth.degCoeff == first.degCoeff):
        print("true")
    else:
        print("false")
