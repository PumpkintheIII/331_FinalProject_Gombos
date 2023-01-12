"""
PLTW CSE 3.3.1 Final Project
Max Gombos
Dice Rolling Application
"""
from dice import Dice

numDieInput = int(input("input number of dice: "))
dieNumInput = int(input("input die number: "))
dice = Dice(numDieInput, dieNumInput)
print(dice)