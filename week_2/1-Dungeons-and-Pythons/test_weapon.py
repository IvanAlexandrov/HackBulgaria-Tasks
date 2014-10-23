import weapon
import unittest


class TestWeapon(unittest.TestCase):
    def setUp(self):
        self.axe = weapon.Weapon("Mighty Axe", 25, 0.2)

    def test_weapon_init(self):
        self.assertEqual(self.axe.type, "Mighty Axe")
        self.assertEqual(25, self.axe.damage)
        self.assertEqual(0.2, self.axe.critical_strike_percent)

    def test_weapon_critical_hit(self):
        result = []
        for i in range(30):
            result.append(self.axe.critical_hit())
        self.assertTrue(True in result)
        self.assertTrue(False in result)


if __name__ == '__main__':
    unittest.main()
