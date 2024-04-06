from random import randint


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
        return(value_of_card, "{0} of {1}".format(card_value, card_family))


    def play(self):
        points = 0
        cards = 0
        while True:
            value, card = self.takeCard()
            cards += 1
            print(card)
            points += value
            print("You now have {0} points.".format(points))
            if points > 21:
                print("BUSTED!")
                break;
            if cards >= 2:
                answer = input("Another card? (y/n)")
                if answer not in ["yes", "y", "yeah", "hell yeah", "you bet"]:
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
        print("Guess a number between {0} and {1}.".format(self.lowest, self.highest))
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
                print("Congratulations, {0}. You guessed the number after {1} attempts.".format(self.name, guesses))
            else:
                if number > guess:
                    print("Guess a higher number")
                else:
                    print("Guess a lower number")


class Hangman:
    def __init__(self, name):
        self.name = name


    def play(self):
        words = ["vinegar", "cider", "lemon", "banana", "orange", "chicken", "giraffe", "lasagne"]
        word = words[randint(0, len(words)-1)]
        hidden_word = ""
        wrong_guesses = ""
        for i in range(0, len(word)):
            hidden_word += "_"
        guesses_left = 8
        while guesses_left > 0 and hidden_word != word:
            if len(wrong_guesses) > 0:
                print("Wrong guesses: {0}".format(wrong_guesses))
            print("{0} guesses left.".format(guesses_left))
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
            print("Congratulations, {0}! You've won the game with {1} guesses left.".format(self.name, guesses_left))
        else:
            print("GAME OVER\nThe correct word was {0}".format(word))


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
            msg = ("Pick a number from 1 to " + str(len(options)) + "\n")
            try:
                playerchoice = int(input(msg)) - 1
            except ValueError:
                print(msg)
            print("Computer picked " + str(options[computerchoice]) + ".")
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
                print("It's a tie with " + str(playerscore) + " points")
            elif playerscore > computerscore:
                print(self.name + " is leading with " + str(playerscore) + " to " + str(computerscore))
            elif computerscore > playerscore:
                print("Computer is leading with " + str(computerscore) + " to " + str(playerscore))
            if input("Do you want to continue? (y/n)") not in ["yes", "y", "yeah", "hell yeah", "you bet"]:
                its_game_on = False
