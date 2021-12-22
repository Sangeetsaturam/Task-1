
#5. Create a class, Car. Have attributes like weight, max_speed, number_of_wheels, service_dates(List of datetime) and methods like get_max_speed(), update_max_speed(), add_service_dare(), get_service_dates() and other methods for fetching and modifying attribute values.

class Car:
    
    def __init__(self,wt,speed,wheels,dates):
        self.weight = wt
        self.max_speed = speed
        self.number_of_wheels = wheels 
        self.service_dates = dates
        
    def get_max_speed(self):
        print("max speed is " ,self.max_speed)
    
    def update_max_speed(self, newSpeed):
        self.max_speed = newSpeed
        
    def add_service_dates(self, newDates):
        self.service_dates.append(newDates)
        
    def get_service_dates(self):
        print(self.service_dates)
        
c = Car(23,120,4,["01/12/2021"])
c.get_max_speed()

c.update_max_speed(140)
c.get_max_speed()

c.get_service_dates()

c.add_service_dates("02/12/2021")
c.get_service_dates()




# OUTPUT:

# max speed is  120
# max speed is  140
# ['01/12/2021']
# ['01/12/2021', '02/12/2021']
