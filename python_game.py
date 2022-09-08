#
# Python: 3.10
#
# Author: Jalen Allison
#
# Purpose: The Tech Academy - Python Course, Creating our first program together.
#          Demonstrating how to pass variables from function to function
#          while producing a functional game.
#
#
#




def start():
    f_name = "Jay"
    l_name = "Tron"
    age = 26
    gender= "Male"
    get_info(f_name,l_name,age,gender)

def get_info(f_name,l_name,age,gender):
    print("My name is {0} {1}. I am {2} year old {3}.".format(f_name,l_name,age,gender))










if __name__ == "__main__":
    start()
