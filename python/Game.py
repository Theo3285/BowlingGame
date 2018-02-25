class Game(object):

    def __init__(self):
        self.rolls = []

    def roll(self, pins):
        self.rolls.append(pins)

    def score(self):
        score = 0
        frameIndex = 0
        for frame in range(0, 10):
            if self.is_strike(frameIndex): # strike
                score += self.strike_bonus(frameIndex)
                frameIndex += 1
            elif self.is_spare(frameIndex):
                score += self.spare_bonus(frameIndex)
                frameIndex += 2
            else:
                score += self.sum_of_all_balls(frameIndex)
                frameIndex += 2
        return score

    def sum_of_all_balls(self, frameIndex):
        return self.rolls[frameIndex] + self.rolls[frameIndex + 1]

    def strike_bonus(self, frameIndex):
        return 10 + self.rolls[frameIndex + 1] + self.rolls[frameIndex + 2]

    def spare_bonus(self, frameIndex):
        return 10 + self.rolls[frameIndex + 2]

    def is_spare(self, frameIndex):
        return self.rolls[frameIndex] + self.rolls[frameIndex + 1] == 10

    def is_strike(self, frameIndex):
        return self.rolls[frameIndex] == 10