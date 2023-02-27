#!/usr/bin/env/python3

"""
frankenstein_game.py

game idea:
you play the creature
and choices are based on the plot of Frakenstein

PATHS:


"""

__author__ = "Ava Teng and Aikam Singh"
__version__ = "2023-02-21"

import time
import os

"""
if val == "a".lower():
    print("")
elif val == "b".lower():
    print("")
elif val == "c".lower():
    print("")

"""

def c():
    os.system("clear")

def s():
    time.sleep(0.5)

def end():
    print("THE END")
    s()
    c()
    val = input("Would you like to play again [y/n]?")
    if val == "y".lower():
        main()
    else:
        print("Thanks for playing! See you again soon!")

def forest():
    print("As you wander through the forest, you come across a house. You decide to hide in a nearby abandoned shed and observe your new friends from afar. \n")
    val = input("What do you do in this situation? \n a) collect firewood \n b) approach your friends \n c) search the shed\n")
    if val == "a".lower():
        print("You find a nearby tree and collect firewood. As you have been observing your friends, you notice that they collect firewood everyday and that it is a taxing task. As a gesture of kindness, you decide to leave some firewood for them to use.")
        s()
        c()
    elif val == "b".lower():
        print("You wait for an opportune moment to approach the cabin.")
        s()
        print(".....")
        s()
        print("You notice that only the old man is in the cabin")

    elif val == "c".lower():
        print("In the shed you find several books which contain old tales such as 'Paradise Lost'. You also decide to check your coat pockets and find a journal which was written by your creator.")
        s()
        print("After reading the books, you learn more about the French language and your creator. You realize that when he created you, he instantly despised you and considered killing you. Enraged by this, you decide to exact revenge on your creator. ")
        
        
def imagery():
    print("You as you venture further and further, your hope diminishes.")
    print("You have encountered several humans, none of whom have greeted you kindly")
    print("As the days go by, you fall deeper and deeper into an existential depression")
    val = input("What do you do? \n a) build a fire and roast marshmallows in a cave, never to see the light of day again \n b) take a walk in nature \n c) try and find a family")
    if val == "a".lower():
        print("In order to start your quiet life of roasting marshmallows, you gather dry wood and light it using two rocks.")
        print("Every day you enjoy the sunrise and the hapiness brought by the gentle warmth.")
        print("And that is how you live: alone, but content, your creator long forgotton.")
        end()
    elif val == "b".lower():
        forest()
    elif val == "c".lower():
        forest()
        
def wake_up():
    print("")
    val = input("Do you(a/b/c): \n a) ask how you were created \n b) go back to sleep \n c) run away\n")
    c()
    s()
    if val == "a".lower():
        print("You were a science experiment created by Victor Frankenstein, a product of his research on resurrecting life.")
        val = input("How do you feel about this? \n a) curious \n b) angry \n c) sad\n")
        c()
        s()
        if val == "a".lower():
            print("You set out into the woods in search of your mysterious creator. Surely he will welcome you with open arms!")
            print("You decide to sed out into the woods in search of your benevolent creator.")
            forest()
        elif val == "b".lower():
            print("You are furious as you realize your creator, your parental guidance, has abandoned you, an innocent and naive creature.")
            print("You decide to exact your revenge")
            forest()
        elif val == "c".lower():
            print("As you realize that you are along, you feel a sadness consume you. You think, 'Perhaps he just lost me and can't find me. I shall find him and we will happily reunite as a family!'")
            print("You decide to venture into the woods to find your family.")
            imagery()
    elif val == "b".lower():
        print("You end the game")
        again = input("Do you want to play again(y/n)?")
        c()
        s()
        if again == "y".lower():
            main()
        else:
            pass
    elif val == "c".lower():
        print("You crash through the window and fall to the ground below. Seeing a forest nearby, you run into it, hiding from your creator and any potential pursuers.")
        s()
        forest()


def main():
    c()
    print("Welcome to the Frankenstein Choose Your Own Adventure game!")
    print("-----------------------------------------------------------")
    s()
    print("As Dr. Frankenstein finalized the creature laying at his feet...")
    s()
    print("The creature began to slowly gain conciousness.")
    s()
    print("First, his mouth twitched,")
    s()
    print("Then, his fingers wiggled,")
    s()
    print("Until finally the creature lifted his gruesome eyelids to reveal sickly yellow eyes.")
    s()
    wake_up()
    

    
if __name__ == "__main__":
    main()

