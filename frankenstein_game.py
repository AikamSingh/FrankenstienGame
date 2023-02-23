#!/usr/bin/env/python3

"""
frankenstein_game.py

game idea:
you play the creature
and choices are based on the plot of Frakenstein

"""

__author__ = "Ava Teng and Aikam Singh"
__version__ = "2023-02-21"

import time
import os

a = "helo"

def c():
    os.system("clear")

def forest():
    print("As you wander through the forest, you come across a house. You decide to hide in a nearby abandoned shed and observe your new friends from afar.")
    val = input("What do you do in this situation? \n a) collect firewood \n b) approach your friends \n c) search the shed\n")
    if val == "a":
        print("You find a nearby tree and collect firewood. As you have been observing your friends, you notice that they collect firewood everyday and that it is a taxing task. As a gesture of kindness, you decide to leave some firewood for them to use.")
        time.sleep(1)
        c()
    if val == "b":
        print("You wait for an opportune moment to approach the cabin.")
        #time.sleep(1)
        print(".....")
        #time.sleep(1)
        print("You notice that only the old man is in the cabin")
        

def main():
    c()
    print("Welcome to the Frankenstein Choose Your Own Adventure game!")
    print("-----------------------------------------------------------")
    #time.sleep(1)
    print("As Dr. Frankenstein finalized the creature laying at his feet...")
    #time.sleep(1)
    print("The creature began to slowly gain conciousness.")
    #time.sleep(1)
    print("First, his mouth twitched,")
    #time.sleep(1)
    print("Then, his fingers wiggled,")
    #time.sleep(1)
    print("Until finally the creature lifted his gruesome eyelids to reveal sickly yellow eyes.")
    #time.sleep(1)
    print("")
    val = input("Do you(a/b/c): \n a) ask how you were created \n b) go back to sleep \n c) run away\n")
    #time.sleep(1)
    if val == "a".lower():
        print("You were a science experiment created by Victor Frankenstein, a product of his research on resurrecting life.")
        val = input("How do you feel about this? \n a) curious \n b) angry \n c) sad\n")
        c()
        if val == "a".lower():
            print("You set out into the woods in search of your mysterious creator. Surely he will welcome you with open arms!")
            print("You decide to sed out into the woods in search of your benevolent creator.")
            forest()
        elif val == "b".lower():
            print("You are furious as you realize your creator, your parental guidance, has abandoned you, an innocent and naive creature.")
            print("You decide to venture into the woods and find this creator in order to exact your revenge")
            forest()
        elif val == "c".lower():
            print("As you realize that you are along, you feel a sadness consume you. You think, 'Perhaps he just lost me and can't find me. I shall find him and we will happily reunite as a family!'")
            print("You decide to venture into the woods to find your family.")
            forest()
    elif val == "b".lower():
        print("You end the game")
        again = input("Do you want to play again(y/n)?")
        if again == "y".lower():
            main()
        else:
            pass
    elif val == "c".lower():
        print("You crash through the window and fall to the ground below. Seeing a forest nearby, you run into it, hiding from your creator and any potential pursuers.")
        forest()

    
if __name__ == "__main__":
    main()

