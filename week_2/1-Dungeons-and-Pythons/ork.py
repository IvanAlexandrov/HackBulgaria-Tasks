from Entity import Entity


class Ork(Entity):
    def __init__(self, name, health, berserk_factor):
        super().__init__(name, health)
        self.berserk_factor = self.__set_berserk_factor(berserk_factor)

    def __set_berserk_factor(self, berserk_factor):
        if berserk_factor > 1 and berserk_factor < 2:
            self.berserk_factor = berserk_factor
        elif berserk_factor < 1:
            self.berserk_factor = 1
        elif berserk_factor > 2:
            self.berserk_factor = 2
        return berserk_factor


