#6. Create multiple objects for this class with different values passed to the constructor.
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def Print(self):
        print("Hello my name is " ,self.name)
        print("Hello my age is " ,self.age)
    
    def update(self,newName,newAge):
        self.name = newName
        self.age = newAge 

p1 = Person("sangeet",23)
p1.Print()

p1.update("kumar",25)
p1.Print()
        
p2= Person("harish",24)
p2.Print()


# Output:
# Hello my name is  sangeet
# Hello my age is  23
# Hello my name is  kumar
# Hello my age is  25
# Hello my name is  harish
# Hello my age is  24

