import random
import string
import requests
#import sys

print("Let's play a SCRABLE mini-game")
class Game:
    def __init__(self):
        self.grid = []
        grid_length = 9
        letters = string.ascii_uppercase
        for i in range(grid_length):
            self.grid.append(random.choice(letters))

    def is_valid(self, word):
        c_word = word.upper()
        if not c_word:
            return False
        letters = self.grid.copy()  # Consume letters from the grid
        for letter in c_word:
            if letter in letters:
                letters.remove(letter)
            else:
                return False
        return self.__check_dictionary(word)

    def __check_dictionary(self, word):
        check = requests.get(f"https://wagon-dictionary.herokuapp.com/{word}")
        response = check.json()
        return response['found']
