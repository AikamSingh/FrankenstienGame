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

def main():
    os.system("clear")
    print("Welcome to the Frankenstein Choose Your Own Adventure game!")
    print("-----------------------------------------------------------")
    time.sleep(1.5)
    print("As Dr. Frankenstein finalized the creature laying at his feet...")
    time.sleep(1.5)
    print("The creature began to slowly gain conciousness.")
    time.sleep(1.5)
    print("First, his mouth twitched,")
    time.sleep(1.5)
    print("Then, his fingers wiggled,")
    time.sleep(1.5)
    print("Until finally the creature lifted his gruesome eyelids to reveal sickly yellow eyes.")
    time.sleep(1.5)
    print("")
    val = input("Enter your value: ")
    print(val)
    print("hello world")

    
if __name__ == "__main__":
    main()

