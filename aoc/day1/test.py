import unittest
from solution.day1 import part2

class TestSTurns(unittest.TestCase):
    def test_1(self):
        #50 -> 99 -> 01 without crossing zero
        count, dial = part2((('R', 49), ('L', 98)))
        self.assertEqual(count, 0)
        self.assertEqual(dial, 1)


    def test_2(self):
        #50 -> 99 -> 00 ending up at zero
        count, dial = part2((('R', 49), ('R', 1)))
        self.assertEqual(count, 1)
        self.assertEqual(dial, 0)


    def test_3(self):
        #50 -> 99 -> 00 -> 01 stopping at zero once
        count, dial = part2((('R', 49), ('R', 1), ('R', 1)))
        self.assertEqual(count, 1)


    def test_4(self):
        #50 -> 01 -> 00 -> 99 stopping at zero once
        count, dial = part2((('R', 49), ('R', 1), ('L', 1)))
        self.assertEqual(count, 1)
        self.assertEqual(dial, 99)


    def test_5(self):
        #50 -> 00 -> and a full rotation ending up at 00 again
        count, dial = part2((('L', 50), ('L', 100)))
        self.assertEqual(count, 2)
        self.assertEqual(dial, 0)


    def test_6(self):
        #50 -> 00 -> and a full rotation ending up at 00 again
        count, dial = part2((('R', 50), ('R', 100)))
        self.assertEqual(count, 2)
        self.assertEqual(dial, 0)


    def test_7(self):
        #50 -> 00 -> and 4 full rotations ending up at 00 again
        count, dial = part2((('L', 50), ('L', 400)))
        self.assertEqual(count, 5)
        self.assertEqual(dial, 0)


    def test_8(self):
        #50 -> 00 -> and 4 full rotations ending up at 00 again
        count, dial = part2((('L', 50), ('R', 400)))
        self.assertEqual(count, 5)
        self.assertEqual(dial, 0)


    def test_9(self):
        #50 and 10 full rotations ending up at 50 again
        count, dial = part2((('R', 1000),))
        self.assertEqual(count, 10)
        self.assertEqual(dial, 50)


if __name__ == '__main__':
    unittest.main()
