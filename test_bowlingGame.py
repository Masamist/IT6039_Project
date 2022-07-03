import unittest
import BowlingGame

class TestBowlingGame(unittest.TestCase):

    def setUp(self):
        self.game = BowlingGame.BowlingGame()

    # Debug:
    # All self.game.rolls -> roll as the function name is incorrect

    # test for game with all gutters
    def testGutterGame(self):
        for i in range(0, 20):
            self.game.roll(0)
        self.assertEqual(self.game.score(), 0)

    # test for game with all single roll score is one
    def testAllOnes(self):
        self.rollMany(1, 20)
        self.assertEqual(self.game.score(), 20)

    # test for game with one spare and all the others are 0
    def testOneSpare(self):
        self.rollMany(5, 2)
        self.game.roll(3)
        self.rollMany(0, 17)
        self.assertEqual(self.game.score(), 16)

    # test for game with one strike and all the others are 0
    def testOneStrike(self):
        self.game.roll(10)
        self.game.roll(4)
        self.game.roll(3)
        self.rollMany(0, 16)
        self.assertEqual(self.game.score(), 24)

    # test for game with one strike and one spare and all the others are 0
    def testOneSpareOneStrike(self):
        self.game.roll(10)
        self.rollMany(5, 2)
        self.rollMany(0, 16)
        self.assertEqual(self.game.score(), 30)

    # test for game with all strikes
    def testPerfectGame(self):
        self.rollMany(10, 12)
        self.assertEqual(self.game.score(), 300)

    # test for game with all spares
    def testAllSpare(self):
        self.rollMany(5, 21)
        self.assertEqual(self.game.score(), 150)

    # test for game with 0 score until 8th frame, then two spares
    def testLastTwoSpare(self):
        self.rollMany(0, 16)
        self.rollMany(5, 5)
        self.assertEqual(self.game.score(), 30)

    # test for game with 0 score until 8th frame, then Four strikes.
    def testLastForeStrike(self):
        self.rollMany(0, 16)
        self.rollMany(10, 4)
        self.assertEqual(self.game.score(), 60)

    # Validation test for input of number of pins before adding into the Array called rolls
    def testError(self):
        self.assertRaises(Exception, self.game.roll, 50)



    # To iterate putting a required number of pins knocked down into Array rolls for required numbers of rolls
    def rollMany(self, pins, rolls):
        for i in range(rolls):

            # Debug:
            # self.game.rolls(pins) should take s from rolls,
            # as the method in the BowlingGame is roll without s
            self.game.roll(pins)

if __name__ == '__main__':
    unittest.main()
