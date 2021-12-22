#4. Call the class method to modify the member variable

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

p = Person("sangeet",23)
p.Print()
p.update("kumar",25)
p.Print()


# OUTPUT:
# Hello my name is  sangeet
# Hello my age is  23
# Hello my name is  kumar
# Hello my age is  25

