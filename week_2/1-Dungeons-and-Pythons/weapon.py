import random


class Weapon(object):
    def __init__(self, type_, damage, critical_strike_percent):
        self.type = type_
        self.damage = damage
        self.critical_strike_percent = critical_strike_percent

    def critical_hit(self):
        if random.random() > self.critical_strike_percent:
            return False
        return True
