#1.Read about how to define a class in python, have a member variable & functions for class

class Person:
    def __init__(self,age):
        self.age = age
    
    def Print(self):
        print("Hello my age is " ,self.age)

p = Person(36)
p.Print()

# Output: 
# Hello my age is  36
