import random
class guessThe_number:
    def __init__(self):
        self.low = 1
        self.high = 1
        self.live = 5
        self.guesses = 0

    def setRange(self, high):
        high = self.high
        if (self.low + 1) < high:
            self.high = high

        else:
            return "Please give a bigger digit"

def play(self):
    if (self.low + 1) < self.high:
        print("Please restart the game")

    while self.guesses < 6:
        self.guesses += 1
        num = random.randint(self.low, self.high)
        guess = int(input("Please guess the number : "))

        if guess == num:
            print("You Won!!")
            break
        else:
            print("Please Try Again")