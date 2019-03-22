from random import randint
from games import Guessthenumber, Hangman


name = input("Hi, there!\nWhat's your name?\n")
games = ["Guess the number", "Hangman"]


print("Hello," + name + ", nice to meet you!")
print("How are you today?")
print("Your name is " + str(len(name)) + " characters long.")

while True:
    answer = input("Would you like to play another game? ")
    if answer not in ["yes", "y", "yeah", "hell yeah", "you bet"]:
        print("Maybe another time.\nBye!")
        exit(0)
    else:
        print("I have " + str(len(games)) + " games available.")
        print("Which game would you like to play? ")
        for game in games:
            print(str(games.index(game)+1), game)
        choice = input("Enter the number of the game: ")
        print(choice)
        if choice == "1":
            g = Guessthenumber(name, 1, 100)
            g.play()
        elif choice == "2":
            h = Hangman(name)
            h.play()
