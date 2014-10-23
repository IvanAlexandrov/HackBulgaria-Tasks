import unittest
import hero


class HeroTests(unittest.TestCase):

    def setUp(self):
        self.hero = hero.Hero("Bron", 100, "DragonSlayer")

    def test_hero_init(self):
        self.assertEqual("Bron", self.hero.name)
        self.assertEqual(100, self.hero.health)
        self.assertEqual("DragonSlayer", self.hero.nickname)

    def test_known_as(self):
        self.assertEqual(self.hero.known_as(), "Bron the DragonSlayer")

    def test_get_health(self):
        self.assertEqual(100, self.hero.get_health())

    def test_is_alive(self):
        self.assertTrue(self.hero.is_alive())
        self.hero.health = 0
        self.assertFalse(self.hero.is_alive())

    def test_take_damage(self):
        self.assertTrue(self.hero.take_damage(30.0))
        result = self.hero.get_health()
        self.assertEqual(70.0, result)
        self.assertFalse(self.hero.take_damage(70))

    def test_take_more_damage_that_he_can(self):
        self.assertFalse(self.hero.take_damage(101))

    def test_take_healing(self):
        self.assertTrue(self.hero.take_healing(10))
        self.hero.health = 10
        self.assertTrue(self.hero.take_healing(10.0))
        self.hero.health = 0
        self.assertFalse(self.hero.take_healing(10.0))

if __name__ == '__main__':
    unittest.main()
