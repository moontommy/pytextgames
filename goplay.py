#!/usr/bin/env python3


# Quick demo for using the pytextgames library
from pytextgames import Guessthenumber, Hangman, Blackjack, RockPaperScissors


playername = input("Hi, there!\nWhat's your name?\n")
games = ["Guess the number", "Hangman", "Blackjack", "Rock, Paper, Scissors"]


print(f"Hello, {playername}, nice to meet you!")
print("How are you today?")
print(f"Your name is {len(playername)} characters long.")


while True:
    answer = input("Would you like to play another game? ")
    if answer not in ["yes", "y", "yeah", "hell yeah", "you bet"]:
        print("Maybe another time.\nBye!")
        exit(0)
    else:
        print(f"I have {len(games)} games available.")
        print("Which game would you like to play? ")
        for game in games:
            print(str(games.index(game)+1), game)
        choice = input("Enter the game number: ")
        if choice == "1":
            g = Guessthenumber(playername, 1, 100)
            g.play()
        elif choice == "2":
            h = Hangman(playername)
            h.play()
        elif choice == "3":
            b = Blackjack(playername)
            b.play()
        elif choice == "4":
            r = RockPaperScissors(playername)
            r.play()
