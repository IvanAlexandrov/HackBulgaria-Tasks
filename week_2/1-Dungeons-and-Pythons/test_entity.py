from hero import Hero
from ork import Ork
from weapon import Weapon
from fight import Fight
from dungeon import Dungeon
import unittest


class EntityTest(unittest.TestCase):
    def setUp(self):
        self.hero = Hero("Bron", 100, "DragonSlayer")
        self.orc = Ork("BronOrk", 100, 1.1)
        self.axe = Weapon("Axe", 12.45, 0.2)
        self.sword = Weapon("Sword of Arthur", 13, 0.5)
        self.battle = Fight(self.hero, self.orc)
        self.dungeon = Dungeon("dungeon.txt")

    def test_hero_init(self):
        self.assertEqual("Bron", self.hero.name)
        self.assertEqual(100, self.hero.health)
        self.assertEqual("DragonSlayer", self.hero.nickname)

    def test_known_as(self):
        self.assertEqual(self.hero.known_as(), "Bron the DragonSlayer")

    def test_get_health(self):
        self.assertEqual(100, self.hero.get_health())
        self.assertEqual(100, self.orc.get_health())

    def test_is_alive(self):
        self.assertTrue(self.hero.is_alive())
        self.hero.health = 0
        self.orc.health = -1
        self.assertFalse(self.orc.is_alive())
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

    def test_orc_init(self):
        self.assertEqual("BronOrk", self.orc.name)
        self.assertEqual(100, self.orc.health)

    def test_ork_berseker(self):
        self.orc._Ork__set_berserk_factor(3)
        self.assertEqual(2, self.orc.berserk_factor)
        self.orc._Ork__set_berserk_factor(0.5)
        self.assertEqual(1, self.orc.berserk_factor)

    def test_has_weapon(self):
        self.assertFalse(self.orc.has_weapon())
        self.orc.equip_weapon(self.axe)
        self.assertTrue(self.orc.has_weapon())

    def test_equip_weapon(self):
        new_weapon = Weapon("Bazuka", 15, 3)
        self.orc.equip_weapon(new_weapon)
        self.assertEqual(new_weapon, self.orc.weapon)

    def test_attack(self):
        self.assertFalse(self.orc.has_weapon())
        self.assertEqual(0, self.orc.attack())
        self.orc.equip_weapon(self.axe)
        self.assertEqual(self.axe.damage, self.orc.attack())

    def test_fight_init(self):
        self.assertEqual(self.battle.hero, self.hero)
        self.assertEqual(self.battle.orc, self.orc)

    def test_simulate_fight(self):
        self.orc.weapon = self.axe
        self.hero.weapon = self.sword
        self.battle.simulate_fight()

    def test_spawn(self):
        self.assertTrue(self.dungeon.spawn('Bron', self.hero))
        self.assertTrue(self.dungeon.spawn('BronOrk', self.orc))
        # self.dungeon.print_map()

    def test_move(self):
        self.dungeon.spawn('Bron', self.hero)
        self.dungeon.spawn('Undead', self.orc)
        self.assertFalse(self.dungeon.move('Bron', 'left'))
        self.assertFalse(self.dungeon.move('Bron', 'up'))
        self.assertTrue(self.dungeon.move('Bron', 'right'))
        self.assertFalse(self.dungeon.move('Undead', 'down'))
        self.assertTrue(self.dungeon.move('Undead', 'up'))
        self.dungeon.print_map()


if __name__ == '__main__':
    unittest.main()
