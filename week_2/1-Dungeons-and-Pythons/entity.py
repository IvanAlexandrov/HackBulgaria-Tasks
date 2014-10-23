class Entity(object):
    def __init__(self, name, health):
        self.name = name
        self.health = health
        self.max_health = health
        self.weapon = "None"

    def get_health(self):
        return self.health

    def is_alive(self):
        return self.get_health() > 0

    def take_damage(self, damage_points):
        self.health -= damage_points
        return self.get_health() > 0

    def take_healing(self, healing_points):
        current_health = self.get_health()
        max_health = self.max_health

        if current_health > 0 and\
           current_health + healing_points <= max_health:
            self.health += healing_points
            return True
        elif current_health + healing_points > max_health:
            self.health = self.max_health
            return True
        elif not self.is_alive():
            return False

    def has_weapon(self):
        if self.weapon == "None":
            return False
        else:
            return True

    def equip_weapon(self, weapon):
        self.weapon = weapon

    def attack(self):
        if not self.has_weapon():
            return 0
        else:
            if self.weapon.critical_hit() is True:
                return self.weapon.damage * 2
            else:
                return self.weapon.damage
