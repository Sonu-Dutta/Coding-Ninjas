class Square:
   def __init__(self,length):
       self.length = length
   def calculateArea(self):
       print(self.length*self.length)
   def printMyType(self):
       print("square")

class Rectangle:
   def __init__(self,length,breath):
       self.length = length
       self.breath = breath
   def calculateArea(self):
       print(self.length*self.breath)
   def printMyType(self):
       print("rectangle")
 
s = Square(5)
s.printMyType()
s.calculateArea()
r = Rectangle(5,4)
r.printMyType()
r.calculateArea()