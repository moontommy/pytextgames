from random import randint


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
