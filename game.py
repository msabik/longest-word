import random
import string
import sys

print("Let's play a SCRABLE mini-game")
class Game:
    def __init__(self):
        self.grid = []
        grid_length = 9
        letters = string.ascii_uppercase
        for i in range(grid_length):
            self.grid.append(random.choice(letters))

    def is_valid(self, word):
        if not word:
            return False
        letters = self.grid.copy()  # Consume letters from the grid
        for letter in word:
            if letter in letters:
                letters.remove(letter)
            else:
                return False
        return True

'''       print(f'Can you find a longest word from this list? {self.grid}')

    def get_user_guess(self):
        self.guess = input()
        return self.guess
'''