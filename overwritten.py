#9. Call an overwritten method and non overwritten method from the object of the extended class.
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



# OUTPUT:

# vehicle is in good condition
# I'm a Vehicle!
# I'm a car!
