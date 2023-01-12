import random

class Dice:

  def __init__(self, numDie, die):
    self.numDie = numDie
    self.die = die
    self.output = 0

  def __str__(self):
    if (self.die == 6):
      self.output = random.randrange(1, 7)
    return str(self.output)
    