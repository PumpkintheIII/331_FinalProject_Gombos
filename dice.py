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
    index = 0
    if (self.die == 6):
      while (index < self.numDie):
        self.output.append(random.randrange(1, 7))
        index = index + 1
    return str(self.output)