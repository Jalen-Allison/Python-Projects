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

# importing required library
import pygame
from pygame.locals import *

# activate the pygame library .
pygame.init()

# set the pygame to determine if a requested display mode is available..
# It will return 0 if the display mode cannot be set. Otherwise it will.. 
# return a pixel depth that best matches the display asked for.
screen = pygame.display.set_mode((500,500),0,32)

# create a surface object, image is drawn on it.
image = pygame.image.load("Images/angryface.jpg").convert()

# Using blit to copy content from one surface to other
screen.blit(image, (10,10))

# paint screen one time
pygame.display.flip()
status = True
while (status):
    # iterate over the list of Event objects
    # that was returned by pygame.event.get() method.
    for i in pygame.event.get():

        # if event object type is QUIT
        # then quitting the pygame
        # and program both.
        if i.type == pygame.QUIT:
            status = False

# deactivates the pygame library            
pygame.quit()


def start(nice=0,mean=0,name=""):
    # get urser's name
    name = describe_game(name)
    nice,mean,name = nice_mean(nice,mean,name)


def describe_game(name):
    """
        check if this is a new game or not.
        If it is new, get the user's name.
        If it is not a new game, thank the player for
        playing again and continue with the game
    """
    # meaning, if we do not already have this user's name,
    # then they are a newq player and we need to get their name
    # "!=" means "not"
    if name != "":
        print("\nThank you for playing again, {}!".format(name))
    else:
        stop = True
        while stop == True:
            if name == "":
                name = input("\nWhat is your name? \n>>> ").capitalize()
                if name != "":
                    print("\nWelcome, {}!".format(name))
                    print("\nIn this game, you will be greeted \nby several different people. \nYou can choose to be nice or mean")
                    print("but at the end of the game your fate \nwill be sealed by your actions.")
                    stop = False
    return name

def nice_mean(nice,mean,name):
    stop = True
    while stop == True:
        show_score(nice,mean,name)
        pick = input("\nA stranger approaches you for a \nconversation. Will you be nice \nor mean? (N/M) \n>>>: ").lower()
        if pick == "n":
            print("\nThe stranger walks away smiling...")
            nice = (nice + 1)
            stop = False
        if pick == "m":
            print ("\nThe stranger glares at you \nmenacingly and storms off...")
            mean = (mean + 1)
            stop = False
    score(nice,mean,name) # pass the 3 variables to the score()


def show_score(nice,mean,name):
    print ("\n{}, your current total: \n({}, Nice) and ({}, Mean)".format(name,nice,mean))


def score(nice,mean,name):
        # score function is being passed the vales stored within the 3 variables
        if nice > 2: # if condition is valid, call win function passing in the variable so it can use them
            win(nice,mean,name)
        if mean > 2: # if condition is valid, call lose function passing in the variable so it can use them
            lose(nice,mean,name)
        else:        # else, call nice_mean function passing in the variables so it can use them
            nice_mean(nice,mean,name)

def win(nice,mean,name):
    # Substitute the {} wildcards with our variable values
    print("\nNice job {}, you win! \nEveryone loves you and you've \nmade lots of friends along the way!".format(name))
    # call again function and pass in our variables
    again(nice,mean,name)

def lose(nice,mean,name):
    # Substitute the {} wildcards with our variable values
    print("\nAhhh too bad, game over! \n{}, you live in a dirty beat-up \nvan by the river, wretched and alone!".format(name))
    # call again function and pass in our variables
    again(nice,mean,name)



def again(nice,mean,name):
    stop = True
    while stop:
        choice = input("\nDo you want to play again? (y/n):\n>>> ").lower()
        if choice == "y":
            stop = False
            reset(nice,mean,name)
        if choice == "n":
            print("\nOh, so sad, sorry to see you go!")
            stop = False
            quit()
        else:
            print("\nEnter ( Y ) for 'YES', ( N ) for 'NO':\n>>> ")

def reset(nice,mean,name):
    nice = 0
    mean = 0
    #Notice, I do not reset the name variable as that same user has eleceted to play again
    start(nice,mean,name)





if __name__ == "__main__":
    start()
