
#parent class
class Car:
    name = ''
    fuel = ''
    speed = ''

    def func(self):
        your_name = input("What is your name? ")
        fuel_type = input("What is fuel type? ")
        max_speed = input("What is max speed? ")
        if (fuel_type == self.fuel and max_speed == self.speed):
            print("Thats a great car, {}!".format(your_name))
        
        
#child class     
class Ferrari(Car):
    def func(self):
        your_name = input("What is your name? ")
        fuel_type = input("What is fuel type? ")
        max_speed = input("What is max speed? ")
        if (fuel_type == self.fuel and max_speed == self.speed):
            print("Thats a great car, {}!".format(your_name))
        else:
            print("Wrong vechile details")
            
#instead of using fuel_type, we're using charge_type.        
class Tesla(Car):
    def func(self):
        your_name - input("What is your name? ")
        charge_type = input("What is charger? ")
        max_speed = input("What is max speed? ")
        if (fuel_type == self.fuel and max_speed == self.speed):
            print("Thats a great car, {}!".format(your_name))
        else:
            print("Wrong vechile details")

Fast = Car()
Fast.func()

Silent = Tesla()
Silent.func()

        

