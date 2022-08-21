class Person:
    def __init__(self, name='', age=1):
        self.name = name
        self.age = age

    def getValue(self):
        return 'The name of the person is '+self.name+' and the age is '+str(self.age)+'.'


name = input()
age = int(input())
person = Person(name, age)
text = person.getValue()
print(text)
