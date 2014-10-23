import random


class Fight(object):
    def __init__(self, Hero, Orc):
        self.hero = Hero
        self.orc = Orc
        self.first_attack = self.__set_attack()

    def __set_attack(self):
        if random.random() < .50:
            return "Hero"
        else:
            return "Orc"

    def simulate_fight(self):
        DAMAGE_FROM_ORC = self.orc.weapon.damage * self.orc.berserk_factor
        DAMAGE_FROM_HERO = self.hero.weapon.damage
        # print(DAMAGE_FROM_ORC, DAMAGE_FROM_HERO)
        while True:
            if self.first_attack == 'Hero':

                if self.hero.attack() == DAMAGE_FROM_HERO * 2:
                    print('Hero makes Critical HIT!')
                    self.orc.take_damage(DAMAGE_FROM_HERO * 2)
                    print('Orc loose ' + str(DAMAGE_FROM_HERO * 2) + " health")
                else:
                    self.orc.take_damage(DAMAGE_FROM_HERO)
                    print('Orc loose ' + str(DAMAGE_FROM_HERO) + " health")
                self.first_attack = 'Orc'
            else:
                if self.orc.attack() == DAMAGE_FROM_ORC * 2:
                    print('Ork makes Critical HIT!')
                    self.hero.take_damage(DAMAGE_FROM_ORC * 2)
                    print('Hero loose ' + str(DAMAGE_FROM_ORC * 2) + " health")
                else:
                    self.hero.take_damage(DAMAGE_FROM_ORC)
                    print("Hero loose " + str(DAMAGE_FROM_ORC) + " health")
                self.first_attack = 'Hero'

            if not self.hero.is_alive():
                print('The hero died.')
                return 'Hero'
            elif not self.orc.is_alive():
                print('One Orc DOWN')
                return 'Orc'
