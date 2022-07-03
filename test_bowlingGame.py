import unittest
import BowlingGame

class TestBowlingGame(unittest.TestCase):

    def setUp(self):
        self.game = BowlingGame.BowlingGame()

    # Debug:
    # All self.game.rolls -> roll as the function name is incorrect

    # test for scores were 0 in all frames
    def testGutterGame(self):
        for i in range(0, 20):
            self.game.roll(0)
        self.assertEqual(self.game.score(), 0)

    # test for all score were 1 in all frames
    def testAllOnes(self):
        self.rollMany(1, 20)
        self.assertEqual(self.game.score(), 20)

    # test for one spare and all 0 score of 9 frames
    def testOneSpare(self):
        self.rollMany(5, 2)
        self.game.roll(3)
        self.rollMany(0, 17)
        self.assertEqual(self.game.score(), 16)

    # test for one strike and all 0 score of 9 frames
    def testOneStrike(self):
        self.game.roll(10)
        self.game.roll(4)
        self.game.roll(3)
        self.rollMany(0, 16)
        self.assertEqual(self.game.score(), 24)

    # test for score including one spare and one strike
    def testOneSpareOneStrike(self):
        self.game.roll(10)
        self.rollMany(5, 2)
        self.rollMany(0, 16)
        self.assertEqual(self.game.score(), 30)

    # test for all scores were strikes in all frames
    def testPerfectGame(self):
        self.rollMany(10, 12)
        self.assertEqual(self.game.score(), 300)

    # test for all score were spare in all frames
    def testAllSpare(self):
        self.rollMany(5, 21)
        self.assertEqual(self.game.score(), 150)

    # test for 0 score until 8th frame, then two spares
    def testLastTwoSpare(self):
        self.rollMany(0, 16)
        self.rollMany(5, 5)
        self.assertEqual(self.game.score(), 30)

    # test for 0 score until 8th frame, then four strikes
    def testLastForeStrike(self):
        self.rollMany(0, 16)
        self.rollMany(10, 4)
        self.assertEqual(self.game.score(), 60)

    # Exception test for input validation of a number of pins knock down is equal or less than 10
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
