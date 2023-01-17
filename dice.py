import random

class Dice:
  roll_id = 0
  def __init__(self, numDie, die):
    self.numDie = numDie
    self.die = die
    self.output = []
    self.roll_id = Dice.roll_id
    Dice.roll_id = Dice.roll_id + 1

  def __str__(self):
    outputString = str(self.numDie) + "d" + str(self.die) + ": " + str(self.output)
    if (len(self.output) > 1):
      totalOutput = 0
      index = 0
      for roll in self.output:
        totalOutput = totalOutput + self.output[index]
        index = index + 1
      outputString = outputString + " Sum = " + str(totalOutput)
    return outputString

  def roll(self):
    index = 0
    while (index < self.numDie):
      rangeNum = self.die + 1
      self.output.append(random.randrange(1, rangeNum))
      index = index + 1
    outputString = str(self.numDie) + "d" + str(self.die) + ": " + str(self.output)
    if (len(self.output) > 1):
      totalOutput = 0
      index = 0
      for roll in self.output:
        totalOutput = totalOutput + self.output[index]
        index = index + 1
      outputString = outputString + " Sum = " + str(totalOutput)
    return outputString