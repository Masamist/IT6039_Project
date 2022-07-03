class BowlingGame:
    def __init__(self):
        # hold all results of rolls for one Ten-Pin bowling game
        self.rolls = []

    def roll(self, pins):
        # Input validation
        if pins > 10:
            raise Exception("A number of pins knocked down must be equal or less than 10.")
        # method to add a number of pins knocked over into the Array self.rolls
        self.rolls.append(pins)

    def score(self):
        # hold scores of the game
        result = 0
        # For counting the roll index
        rollIndex = 0

        # Calculating each frames score and add to result
        for frameIndex in range(10):

            # Debug:
            # passing value of all conditions that are incorrect
            # when you add the value in result, it should be (rollIndex) ->(self.rolls[rollIndex])
            # e.g., + strikeScore(self.rolls[rollIndex])

            # hold scores of first and second rolls of a frame
            totalPinsInFrame = self.rolls[rollIndex] + self.rolls[rollIndex + 1]

            # Strike condition
            # if the first roll's score is 10 pins, this means strike
            if self.rolls[rollIndex] == 10:
                # calculate the strike score
                # this "totalPinsInFrame" is included in the next frame's first roll,
                # so adding the next frame's second roll is a strike score
                result += totalPinsInFrame + self.rolls[rollIndex + 2]
                # add 1 to rollIndex for moving onto next roll calculation
                rollIndex += 1

            else:
                # Normal frame score and Spare condition
                result += totalPinsInFrame
                # Checking Spare condition
                # Adding both first and second frame's score equal 10, then this is spare.
                if totalPinsInFrame == 10:
                    # If it is spare, get extra point of the first roll in the next frame
                    result += self.rolls[rollIndex + 2]
                # add 2 to rollIndex for moving onto next roll calculation
                rollIndex += 2

        return result

    # Refactor:
    # These five functions are simply added to the original if statement
    # to remove unnecessary function

    # def isStrike(self, rollIndex):
    #     return self.rolls[rollIndex] == 10

    # def isSpare(self, rollIndex):
    #     return self.rolls[rollIndex] + self.rolls[rollIndex+1] == 10

    # def strikeScore(self, rollIndex):
    #     return 10 + self.rolls[rollIndex + 1] + self.rolls[rollIndex + 2]

    # def spareScore(self, rollIndex):
    #     return 10 + self.rolls[rollIndex + 2]

    # def frameScore(self, rollIndex):
    #     return self.rolls[rollIndex] + self.rolls[rollIndex + 1]
