from random import randint
import requests

YES_ANSWERS = ["yes", "y", "yeah", "hell yeah", "you bet"]


class Blackjack:
    def __init__(self, name):
        self.name = name


    def takeCard(self):
        card_families = ("Hearts", "Diamonds", "Clubs", "Spades")
        card_no = randint(0, 52)
        card_family = card_families[int((card_no - .1) / 13)]
        card_value = card_no % 13
        if card_value == 1:
            card_value = "Ace"
            value_of_card = 1
        elif card_value == 11:
            card_value = "Jack"
            value_of_card = 10
        elif card_value == 12:
            card_value = "Queen"
            value_of_card = 10
        elif card_value == 0:
            card_value = "King"
            value_of_card = 10
        else:
            value_of_card = card_value
        return(value_of_card, f"{card_value} of {card_family}")


    def play(self):
        points = 0
        cards = 0
        while True:
            value, card = self.takeCard()
            cards += 1
            print(card)
            points += value
            print(f"You now have {points} points.")
            if points > 21:
                print("BUSTED!")
                break;
            if cards >= 2:
                answer = input("Another card? (y/n)")
                if answer not in YES_ANSWERS:
                    break;


class Guessthenumber:
    # def __init__(self):
    #     self.name = "dude"
    #     self.lowest = 1
    #     self.highest = 100
    #
    #
    # def __init__(self, name):
    #     self.name = name
    #     self.lowest = 1
    #     self.highest = 100


    def __init__(self, name, lowest, highest):
        self.name = name
        self.lowest = lowest
        self.highest = highest


    def play(self):
        print(f"Guess a number between {self.lowest} and {self.highest}.")
        number = randint(self.lowest, self.highest)
        guess = 0
        guesses = 0
        while guess != number:
            try:
                guess = int(input("What's your guess? "))
            except all:
                print(err)
            guesses += 1
            if guess == number:
                print("That's correct!")
                print(f"Congratulations, {self.name}. You guessed the number after {guesses} attempts.")
            else:
                if number > guess:
                    print("Guess a higher number")
                else:
                    print("Guess a lower number")


class Hangman:
    def __init__(self, name):
        self.name = name


    def play(self):
        words = requests.get("https://www.mit.edu/~ecprice/wordlist.10000").content.splitlines()
        word_choices = []
        for word in words:
            word = str(word).replace('b', '')
            if len(word) > 4:
                word_choices += [word]
        word = word_choices[randint(0, len(word_choices) - 1)]
        hidden_word = "_" * len(word)
        wrong_guesses = ""
        guesses_left = 8
        while guesses_left > 0 and hidden_word != word:
            if len(wrong_guesses) > 0:
                print(f"Wrong guesses: {wrong_guesses}")
            print(f"{guesses_left} guesses left.")
            print(hidden_word)
            guess = input("Enter a letter: ")
            if guess in word:
                print("OK")
                # Save locations of all hits in list
                guess_location = ([pos for pos, char in enumerate(word) if char == guess])
                for g in guess_location:
                    # Replace underscores by actual character
                    hidden_word = hidden_word[:g] + guess + hidden_word[g+1:]
            else:
                print("Wrong!")
                wrong_guesses += guess
                guesses_left -= 1
        if hidden_word == word:
            print(f"Congratulations, {self.name}! You've won the game with {guesses_left} guesses left.")
        else:
            print(f"GAME OVER\nThe correct word was {word}")


class RockPaperScissors:
    def __init__(self, name):
        self.name = name


    def play(self):
        options = ["rock", "paper", "scissors"]
        playerscore = 0
        computerscore = 0
        its_game_on = True
        while its_game_on:
            computerchoice = randint(0, 2)
            print("What's your choice?")
            for o in options:
                print(str(options.index(o) + 1), o.capitalize())
            msg = (f"Pick a number from 1 to {len(options)}\n")
            try:
                playerchoice = int(input(msg)) - 1
            except ValueError:
                print(msg)
            print(f"Computer picked {options[computerchoice]}.")
            # Calculate winner
            if playerchoice == computerchoice:
                print("It's a tie!")
            if playerchoice == 0:
                # Player picks rock
                if computerchoice == 1:
                    # Computer picks paper
                    print("Paper covers rock.\nComputer wins!")
                    computerscore += 1
                elif computerchoice == 2:
                    # Computer picks scissors
                    print("Rock smashes scissors.\nPlayer wins!")
                    playerscore += 1
            elif playerchoice == 1:
                # Player picks paper
                if computerchoice == 0:
                    # Computer picks rock
                    print("Paper covers rock.\nPlayer wins!")
                    playerscore += 1
                elif computerchoice == 2:
                    # Computer picks scissors
                    print("Scissors cut paper.\nComputer wins!")
                    computerscore += 1
            elif playerchoice == 2:
                # Player picks scissors
                if computerchoice == 0:
                    # Computer picks rock
                    print("Rock smashes scissors.\nComputer wins!")
                    computerscore += 1
                elif computerchoice == 1:
                    # Computer picks paper
                    print("Scissors cut paper.\nPlayer wins!")
                    playerscore += 1
            else:
                print("That's not a valid option.")
            # Print score
            if playerscore == computerscore:
                print(f"It's a tie with {playerscore} points")
            elif playerscore > computerscore:
                print(f"{self.name} is leading with {playerscore} to {computerscore}")
            elif computerscore > playerscore:
                print(f"Computer is leading with {computerscore} to {playerscore}")
            if input("Do you want to continue? (y/n)") not in YES_ANSWERS:
                its_game_on = False
