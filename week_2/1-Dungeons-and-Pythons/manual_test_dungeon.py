from dungeon import Dungeon
from hero import Hero
from ork import Ork
from weapon import Weapon

d = Dungeon('dungeon.txt')
hero = Hero('Manson', 120, 'Captain')
orc = Ork('FishHead', 100, 1.01)
orc.weapon = Weapon('Axe', 12, 0.2)
hero.weapon = Weapon('Gun', 20, 0.1)
print(hero.known_as() + " IS HERE")
print(d.move("FishHead", 'right'))
d.spawn('Manson', hero)
d.spawn('FishHead', orc)
d.move('Manson', 'right')
d.move('Manson', 'down')
d.move('Manson', 'down')
d.move('Manson', 'down')
d.move('Manson', 'right')
d.move('Manson', 'right')
d.move('Manson', 'right')
d.move('Manson', 'right')
d.move('Manson', 'up')
d.move('Manson', 'up')
d.move('Manson', 'up')
d.move('Manson', 'right')
d.move('FishHead', 'up')
d.move('FishHead', 'up')
d.move('FishHead', 'up')
d.move('FishHead', 'up')
d.move('FishHead', 'left')
d.move('FishHead', 'left')
d.move('FishHead', 'left')
d.print_map()
