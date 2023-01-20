import random #imports random function

class Dice: #defines Dice class
  roll_id = 0 #initializes roll_id
  def __init__(self, numDie, die): #defines initial method
    #initial method creates variables and lists to be used in other parts of the class
    self.numDie = numDie #number of dice
    self.die = die #type of die
    self.output = [] #list of dice outputs
    #updates roll_id:
    self.roll_id = Dice.roll_id 
    Dice.roll_id = Dice.roll_id + 1

  def __str__(self): #defines string method
    #string method is returned when other parts of the program call the class as a string
    #creates a string variable that holds the user input and roll output
    outputString = str(self.numDie) + "d" + str(self.die) + ": " + str(self.output)
    if (len(self.output) > 1):
      #if there are more than 1 die being rolled, adds the output together for user
      totalOutput = 0 #initializes totalOutput
      index = 0 #initializes index
      for roll in self.output: #for all dice rolled:
        totalOutput = totalOutput + self.output[index]
        #add roll output to output of other dice rolled
        index = index + 1 #updates index
      outputString = outputString + " Sum = " + str(totalOutput)
      #updates outputString to include sum of rolls
    return outputString

  def roll(self): #defines roll method
    #roll method rolls the inputed dice
    index = 0 #intializes index variable
    while (index < self.numDie): #for every inputed die:
      rangeNum = self.die + 1 #initializes rangeNum variable
      self.output.append(random.randrange(1, rangeNum))
      #rolls die and adds its output to the output list
      index = index + 1 #updates index
    outputString = str(self.numDie) + "d" + str(self.die) + ": " + str(self.output)
    #formats output in a string variable
    if (len(self.output) > 1): #if more than 1 die rolled:
      #if there are more than 1 die being rolled, adds the output together for user
      totalOutput = 0 #initializes totalOutput
      index = 0 #initializes index
      for roll in self.output: #for every die rolled:
        totalOutput = totalOutput + self.output[index]
        #add die output to output of previous dice
        index = index + 1 #update index
      outputString = outputString + " Sum = " + str(totalOutput)
      #update outputString to include the sum of dice rolled
    return outputString