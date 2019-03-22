from random import randint


class Guessthenumber:
    def __init__(self):
        self.name = "dude"
        self.lowest = 1
        self.highest = 100


    def __init__(self, name):
        self.name = name
        self.lowest = 1
        self.highest = 100


    def __init__(self, name, lowest, highest):
        self.name = name
        self.lowest = lowest
        self.highest = highest


    def play(self):
        print("Guess a number between " + str(self.lowest) + " and " + str(self.highest))
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
                print("Congratulations, " + self.name + ". You guessed the number after " + str(guesses) + " attempts.")
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
        for i in range(0, len(word)):
            hidden_word += "_"
        guesses_left = 8
        while guesses_left > 0 and hidden_word != word:
            print(str(guesses_left) + " guesses left.")
            print(hidden_word)
            guess = input("Enter a letter: ")
            if guess in word:
                print("OK")
                guess_location = word.find(guess)
                hidden_word = hidden_word[:guess_location] + guess + hidden_word[guess_location+1:]
            else:
                print("Wrong!")
                guesses_left -= 1
        if hidden_word == word:
            print("Congratulations, " + self.name + "! You won the game with " + str(guesses_left) + " guesses left.")
        else:
            print("GAME OVER\nThe correct word was " + word)
