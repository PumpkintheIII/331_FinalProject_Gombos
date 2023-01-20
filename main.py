"""
PLTW CSE 3.3.1 Final Project
Max Gombos
Dice Rolling Application
"""
from dice import Dice #imports Dice class
import datetime #imports datetime (for logging when dice rolled)


rollArchive = []

def roll(): #defines function to roll a die
  dieInput = "" #initialize dieInput variable
  print("\nRoll a Dice!\n\
For more information on how to roll a dice, check out the help page. To exit, enter q.")
  while (dieInput != "q"): #unless quit:
    dieInput = input("Input: ") #input for user to specify die to roll
    if (dieInput != "q" and dieInput != ""): #unless quit:
      try: #when executing code, looks for errors
        splitInput = dieInput.split("d")
        #split input into two usable numbers
        dice = Dice(int(splitInput[0]), int(splitInput[1]))
        #sets the dice to entered values
        print("\t", dice.roll()) #rolls dice
        rollArchive.append(str(datetime.datetime.now()) + ", " + str(dice)) #adds roll to the roll archive
      except: #if error, tells user
        print("There was an error, please enter a valid command.")
  

def rollHistory(): #defines function to check past rolls
  quitCheck = "" #intitializes quit check variable
  while (quitCheck != "q"): #unless quit:
    print("\nPrevious rolls (enter q to go back to menu):")
    index = 0 #initializes index
    for roll in rollArchive: #for every roll in archvie
      print("\t" + str(index) + ": " + str(rollArchive[index]))
      #print roll
      index += 1 #update index
    try: #when code runs, checks for errors
      quitCheck = input("Enter q to go back: ") #allow user to go back to menu
      if (quitCheck != "q"): #if user doesn't enter q:
        #tells user how to go back to menu
        print("To go back to menu, enter q.")
    except: #if error:
      print("There was an error, please enter a valid response.")

def viewHelp(): #defines function to display help info
  print("\nTo roll a dice, input the dice type. Dice types:\n\
\t1d4: 4 Sided Die\n\
\t1d6: 6 Sided Die\n\
\t1d8: 8 Sided Die\n\
\t1d9: 9 Sided Die\n\
\t1d12: 12 Sided Die\n\
\t1d10: 10 Sided Die\n\
\t1d20: 20 Sided Die\n\
\t1d100: 100 Sided Die\n\
To roll multiple dice at a time, change the number before the d to how many dice you wish to roll.")
  #info on how to format the inputs




print("Dice Roller\n\
Enter the number corresponding with what you would like to do\n\
\t1: Roll Dice\n\
\t2: View Previous Rolls\n\
\t3: Help\n\
\t4: Quit") #menu
choice = input("Input: ")
#allows user to pick what they want to do
try: #when code runs, checks for errors:
  if (choice == "q"):
    #if user input "q" instead of 4, changes it
    choice = 4
  else:
    #changes choice variable to an integer instead of a string
    choice = int(choice)
except: #if there was an error:
  print("There was an error, please enter a valid response.")

while (choice != 4): #unless quit:
  if (choice == 1):
    #lets the user roll dice
    roll()
  elif (choice == 2):
    #lets the user view roll history
    rollHistory()
  elif (choice == 3):
    #lets the user view help
    viewHelp()

  #allow user to use the menu again:
  print("\nDice Roller\n\
Enter the number corresponding with what you would like to do\n\
\t1: Roll Dice\n\
\t2: View Previous Rolls\n\
\t3: Help\n\
\t4: Quit")
  choice = input("Input: ")
  try: #when code runs, check for errors:
    if (choice == "q"):
      choice = 4
    else:
      choice = int(choice)
  except: #if there was an error:
    print("There was an error, please enter a valid response.")