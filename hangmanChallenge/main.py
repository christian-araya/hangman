"""
Modify the game, so a word is selected randomly from a list of words
"""

import random
import hangmanFxn


myList = ["tacos", "french fries", "orca", "jaguar", "race car"]
indexNumb = random.randint(0,4)
hangmanFxn.hangman(myList[indexNumb])
