"""
PLTW CSE 3.3.1 Final Project
Max Gombos
Dice Rolling Application
"""
from dice import Dice
import datetime
import os

rollArchive = []

def roll():
  dieInput = ""
  print("Roll a Dice!\n\
For more information on how to roll a dice, check out the help page. To exit, enter q.")
  while (dieInput != "q"):
    dieInput = input("Input: ")
    if (dieInput != "q" and dieInput != ""):
      splitInput = dieInput.split("d")
      dice = Dice(int(splitInput[0]), int(splitInput[1]))
      print(dice.roll())
      rollArchive.append(str(datetime.datetime.now()) + ", " + str(dice))
    else:
      print("Please enter a valid response. See help for more information.")
  os.system('clear')

def rollHistory():
  quitCheck = ""
  while (quitCheck != "q"):
    if (len(rollArchive) > 10):
        index = 0
        while (quitCheck != "q"):
          os.system('clear')
          print("Preivous rolls:")
          counter = 0
          page = index
          while (counter < 10):
            print("\t" + str(index) + ": " + rollArchive[index])
            index = index + 1 
            counter = counter + 1
          print("(Showing rolls " + str(page) + " - " + str(index) + ")")
          quitCheck = input("Enter > to move to next page. Enter q to go back to menu. ")
    else:
      print("Previous rolls (enter q to go back to menu):")
      index = 0
      for roll in rollArchive:
        print("\t" + str(index) + ": " + rollArchive[index])
        index = index + 1
      quitCheck = input("")

print("Dice Roller\n\
Enter the number corresponding with what you would like to do\n\
\t1: Roll Dice\n\
\t2: View Previous Rolls\n\
\t3: Help\n\
\t4: Quit")
welcome = int(input("Input: "))

while (welcome != 4):
  if (welcome == 1):
    os.system('clear')
    roll()
  elif (welcome == 2):
    os.system('clear')
    rollHistory()
  elif (welcome == 3):
    os.system('clear')
    print("To roll a dice, input the dice type. Dice types:\n\
\t1d4: 4 Sided Die\n\
\t1d6: 6 Sided Die\n\
\t1d8: 8 Sided Die\n\
\t1d9: 9 Sided Die\n\
\t1d12: 12 Sided Die\n\
\t1d10: 10 Sided Die\n\
\t1d20: 20 Sided Die\n\
\t1d100: 100 Sided Die\n\
To roll multiple dice at a time, change the number before the d to how many dice you wish to roll.")
  
  print("Dice Roller\n\
Enter the number corresponding with what you would like to do\n\
\t1: Roll Dice\n\
\t2: View Previous Rolls\n\
\t3: Help\n\
\t4: Quit")
  welcome = int(input("Input: "))