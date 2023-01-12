"""
PLTW CSE 3.3.1 Final Project
Max Gombos
Dice Rolling Application
"""
from dice import Dice

def roll():
  dieInput = ""
  print("Roll a Dice!\n\
For more information on how to roll a dice, check out the help page. To exit, enter q.")
  while (dieInput != "q"):
    dieInput = input("Input: ")
    if (dieInput != "q"):
      splitInput = dieInput.split("d")
      dice = Dice(int(splitInput[0]), int(splitInput[1]))
      print(dice)

print("Dice Roller\n\
Enter the number corresponding with what you would like to do\n\
\t1: Roll Dice\n\
\t2: View Previous Rolls\n\
\t3: Help\n\
\t4: Quit")
welcome = int(input("Input: "))

while (welcome != 4 and welcome != "q"):
  if (welcome == 1):
    roll()
  elif (welcome == 3):
    print("To roll a dice, input the dice type. Dice types:\n\
\t1d4: 4 Sided Die\n\
\t1d6: 6 Sided Die\n\
\t1d8: 8 Sided Die\n\
\t1d9: 9 Sided Die\n\
\t1d12: 12 Sided Die\n\
\t1d10: 10 Sided Die\n\
\t1s20: 20 Sided Die\n\
\t1d100: 100 Sided Die\n\
To roll multiple dice at a time, change the number before the d to how many dice you wish to roll.")
  
  print("Dice Roller\n\
Enter the number corresponding with what you would like to do\n\
\t1: Roll Dice\n\
\t2: View Previous Rolls\n\
\t3: Help\n\
\t4: Quit")
  welcome = int(input("Input: "))