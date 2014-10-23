import unittest
import ork


class OrkTests(unittest.TestCase):

    def setUp(self):
        self.ork = ork.Ork("BronOrk", 100, 1.0)

    def test_ork_init(self):
        self.assertEqual("BronOrk", self.ork.name)
        self.assertEqual(100, self.ork.health)

    def test_ork_berseker(self):
        self.ork._Ork__set_berserk_factor(3)
        self.assertEqual(2, self.ork.berserk_factor)
        self.ork._Ork__set_berserk_factor(0.5)
        self.assertEqual(1, self.ork.berserk_factor)


if __name__ == '__main__':
    unittest.main()
