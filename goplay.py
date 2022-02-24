#!/usr/bin/env python3


# Quick demo for using the pytextgames library
from pytextgames import Guessthenumber, Hangman, Blackjack


playername = input("Hi, there!\nWhat's your name?\n")
games = ["Guess the number", "Hangman", "Blackjack"]


print("Hello, {0}, nice to meet you!".format(playername))
print("How are you today?")
print("Your name is {0} characters long.".format(len(playername)))


while True:
    answer = input("Would you like to play another game? ")
    if answer not in ["yes", "y", "yeah", "hell yeah", "you bet"]:
        print("Maybe another time.\nBye!")
        exit(0)
    else:
        print("I have games available.".format(len(games)))
        print("Which game would you like to play? ")
        for game in games:
            print(str(games.index(game)+1), game)
        choice = input("Enter the number of the game: ")
        print(choice)
        if choice == "1":
            g = Guessthenumber(playername, 1, 100)
            g.play()
        elif choice == "2":
            h = Hangman(playername)
            h.play()
        elif choice == "3":
            b = Blackjack(playername)
            b.play()
