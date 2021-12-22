# 7. Extending a base class.
# 8. Override a method. 
# 10. Create a base class Vehicle. Extend the class and create Car and Bus. create objects for these classes.

class Vehicle():  #base class
    def description(self):
        print("I'm a Vehicle!")
        
    def goodVehicle(self):
        print("vehicle is in good condition")

# subclass
class Car(Vehicle):
    def description(self):
        print("I'm a car!")
        
class Bus(Vehicle):
    def description(self):
        print("I'm a bus!")         
        
        
# create an object from each class
v = Vehicle()
c = Car()
b = Bus()

c.goodVehicle()

#override
v.description()
c.description()
b.description()


# OUTPUT:
# vehicle is in good condition
# I'm a Vehicle!
# I'm a car!
# I'm a bus!
