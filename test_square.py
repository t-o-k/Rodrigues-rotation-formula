import unittest
from square import sqr


class Test_square(unittest.TestCase):


    def setUp(self):
        pass


    def test_sqr(self):
        v = 12.0
        vv = 144.0
        self.assertEqual(sqr(v), vv)


if __name__ == "__main__":
    unittest.main()

