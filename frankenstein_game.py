#!/usr/bin/env/python3

"""
frankenstein_game.py

game idea:
you play the creature
and choices are based on the plot of Frakenstein

CURRENT WIP


"""

__author__ = "Ava Teng and Aikam Singh"
__version__ = "2023-02-21"

import time
import os
import sys

"""
if val == "a".lower():
    print("")
elif val == "b".lower():
    print("")
elif val == "c".lower():
    print("")

"""

s = 0
k = 0
n = 0

def print_slowly(text):
    for c in text:
        print(c, end = "")
        sys.stdout.flush()
        time.sleep(1)

def c():
    os.system("clear")

def sl():
    time.sleep(0.5)

def nice(i):
    global n
    n += i
    print(n)
    print(str(i) + " NICENESS POINTS")

def survival(i):
    global s
    s += i
    print(str(i) + " SURVIVAL POINTS")

def knowledge(i):
    global k
    k += i
    print(str(i) + " KNOWLEDGE POINTS")

def end():
    print("THE END")
    sl()
    c()
    print("HERE ARE YOUR STATISTICS FOR THE GAME: ")
    # print out the stats of the game based on the options
    print("Niceness points: " + str(n))
    print("Survival points: " + str(s))
    print("Knowledge points: " + str(k))
    #print("_____ points: " + str(something idk yet))

    val = input("Would you like to play again [y/n]?")
    if val == "y".lower():
        main()
    else:
        print("Thanks for playing! See you again soon!")

def town():
    
    c()

def cabin(): 
    print("You see a cabin as you wander through the forest. You decide to knock on the door and try to talk to the inhabitants.")
    sl()
    print("An old man opens the door and asks, 'Who's there?'");
    sl()
    print("You notice that the old man is not looking at anything in particular, so you come to the conclusion that his sight is impared in some way. Knowing how your creator rejected you once he saw you, you decide to take advantage of this blindess and try to win his sympathy.")
    sl()
    print("While you are recounting your journeys to the old man, son, daughter in law, and daughter walk in.")
    sl()
    print("The son, not aware of the situation and your motives, decides to start beating you with a stick and chasing you out of the house.")
    val = input("What do you do? \n a) run away into the woods \n b) try to reason with the son \n c) fight back")
    if val == "a".lower():
        print("You sprint as fast as possible out of the house. You can't believe how they treated you, even though you shouldn't be suprised since it is the same way that your creator reacted to you. Saddened by this, you decide to move on from the cabin and try to find your creator again.")
        nice(10)
        town()
    elif val == "b".lower():
        print("You try to explain your situation to the son, but to no avail. You decide to leave the house and continue your journey.")
        survival(10)
        town()
    elif val == "c".lower():
        print("You decide to fight back, clawing at your attacker with all your might. The dust settles, and your attacker looks wounded, but he seems like he will still live. You decide to run away from the house before he could retaliate again.")
        sl()
        print(sl)
        survival(20)
        nice(-10)
        town()

def forest():
    print("As you wander through the forest, you come across a house. You decide to hide in a nearby abandoned shed and observe your new friends from afar. \n")
    val = input("What do you do in this situation? \n a) collect firewood \n b) approach your friends \n c) search the shed\n")
    if val == "a".lower():
        print("You find a nearby tree and collect firewood. As you have been observing your friends, you notice that they collect firewood everyday and that it is a taxing task. As a gesture of kindness, you decide to leave some firewood for them to use.")
        sl()
        c()
    elif val == "b".lower():
        print("You wait for an opportune moment to approach the cabin.")
        sl()
        print_slowly("......")
        print()
        print("You notice that only the old man is in the cabin. Now is your chance!")
        print("When he opens thr door, you see that he is not looking at anything in particular, so you come to the conclusion that his sight is impared in some way. Knowing how your creator rejected you once he saw you, you decide to take advantage of this blindess and try to win his sympathy.")
        sl()
        print("While you are recounting your journeys to the old man, son, daughter in law, and daughter walk in.")
        
    elif val == "c".lower():
        print("In the shed you find several books which contain old tales such as 'Paradise Lost'. You also decide to check your coat pockets and find a journal which was written by your creator.")
        sl()
        print("After reading the books, you learn more about the French language and your creator. You realize that when he created you, he instantly despised you and considered killing you. Enraged by this, you decide to exact revenge on your creator. ")
        survival(100)


def imagery():
    print("You as you venture further and further, your hope diminishes.")
    print("You have encountered several humans, none of whom have greeted you kindly")
    print("As the days go by, you fall deeper and deeper into an existential depression")
    val = input("What do you do? \n a) build a fire and roast marshmallows in a cave, never to see the light of day again \n b) take a walk in nature \n c) try and find a family\n")
    if val == "a".lower():
        print("In order to start your quiet life of roasting marshmallows, you gather dry wood and light it using two rocks.")
        print("Every day you enjoy the sunrise and the hapiness brought by the gentle warmth.")
        print("And that is how you live: alone, but content, your creator long forgotton.")
        end()
    elif val == "b".lower():
        cabin()
    elif val == "c".lower():
        forest()
        
def wake_up():
    print("")
    val = input("Do you(a/b/c): \n a) ask how you were created \n b) go back to sleep \n c) run away\n")
    c()
    sl()
    if val == "a".lower():
        print("You were a science experiment created by Victor Frankenstein, a product of his research on resurrecting life.")
        val = input("How do you feel about this? \n a) curious \n b) angry \n c) sad\n")
        c()
        sl()
        if val == "a".lower():
            print("You set out into the woods in search of your mysterious creator. Surely he will welcome you with open arms!")
            forest()
        elif val == "b".lower():
            print("You are furious as you realize your creator, your parental guidance, has abandoned you, an innocent and naive creature.")
            print("You decide to exact your revenge")
            print("But first, you must quench your thirst and satisfy your hunger! Perhaps you can find some in the forest...")
            val = input("Would you like to have for lunch? \n a)some berries \n b)some fish \n c)leaves\n")
            c()
            sl()
            if val == "a".lower():
                print("Searching", end = "")
                print_slowly("......")
                print("Look! Some wild raspberries!")
                print("You pick a bunch and eat them while continuing to walk, until, ", end = "")
                forest()
            elif val == "b".lower():
                print("Hmm... there should be a river nearby... I swear you passed one...")
                sl()
                print("Aha! There it is! Let's go catch some fish!")
                for i in range(3):
                    sl()
                    print("><(((°>")
                """print("        )       ")
                print("       ((       ")
                print("      ))((      ")
                print("(___(__(())___()")
                print("(___________())")"""
                cabin()
            else:
                print("Interesting choice... not what I would have picked but okay...")
                print("You do you, friend!")
                survival(-50)
                imagery()
        elif val == "c".lower():
            print("As you realize that you are along, you feel a sadness consume you. You think, 'Perhaps he just lost me and can't find me. I shall find him and we will happily reunite as a family!")
            print("You decide to venture into the woods to find your family.")
            imagery()
    elif val == "b".lower():
        print("Great! Naps (or in this case an everlasting sleep) are amazing!")
        sl()
        again = input("Do you want to play again(y/n)?")
        c()
        sl()
        if again == "y".lower():
            main()
        else:
            pass
    elif val == "c".lower():
        print("You crash through the window and fall to the ground below. Seeing a forest nearby, you run into it, hiding from your creator and any potential pursuers.")
        sl()
        forest()


def main():
    c()
    print("Welcome to the Frankenstein Choose Your Own Adventure game!")
    print("________________________________________________________________________________________________________________________________")
    sl()
    print("As Dr. Frankenstein finalized the creature laying at his feet...")
    sl()
    print("The creature began to slowly gain conciousness.")
    sl()
    print("First, his mouth twitched,")
    sl()
    print("Then, his fingers wiggled,")
    sl()
    print("Until finally the creature lifted his gruesome eyelids to reveal sickly yellow eyes.")
    sl()
    wake_up()
    

    
if __name__ == "__main__":
    main()

