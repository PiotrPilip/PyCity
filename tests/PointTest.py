import unittest

from common.Point import Point


class TestPoint(unittest.TestCase):
    def test_creation_2_args(self):
        p = Point(1, 2)
        self.assertEqual(p.x, 1)
        self.assertEqual(p.y, 2)
        self.assertEqual(p.xy, (1, 2))

    def test_creation_from_tuple(self):
        p = Point((1, 2))
        self.assertEqual(p.x, 1)
        self.assertEqual(p.y, 2)
        self.assertEqual(p.xy, (1, 2))

    def test_addition(self):
        p1 = Point(1, 2)
        p2 = Point(2, 4)
        p3 = p1 + p2
        self.assertEqual(p3.x, 3)
        self.assertEqual(p3.y, 6)
        self.assertEqual(p3.xy, (3, 6))

    def test_subtraction(self):
        p1 = Point(1, 2)
        p2 = Point(2, 4)
        p3 = p1 - p2
        self.assertEqual(p3.x, -1)
        self.assertEqual(p3.y, -2)
        self.assertEqual(p3.xy, (-1, -2))


if __name__ == '__main__':
    unittest.main()
