from hero import Hero
from ork import Ork
from fight import Fight


class Dungeon(object):
    """
    TODO:
        - implement died body removal from map
        - implement randdom GIFT of heal after battle ends
    """
    def __init__(self, map_):
        self.map = map_
        self.dungeon_map = open(self.map, 'r')
        content = self.dungeon_map.read()
        self.current_map = [list(line) for line in content.splitlines()]
        self.dungeon_map.close()
        self.players = {}

    def print_map(self):
        for row in self.current_map:
            elements = ''
            for col in row:
                elements += col
            print(elements)

    def spawn(self, player_name, entity):
        if isinstance(entity, Hero):
            sign = 'H'
            self.players[player_name] = {'type': 'Hero', "class": entity, "sign": sign}
            self.update_start_points(sign)
            return True
        elif isinstance(entity, Ork):
            sign = 'O'
            self.players[player_name] = {"type": 'Orc', "class": entity, "sign": sign}
            self.update_start_points(sign)
            return True
        else:
            return False

    def update_start_points(self, sign):
        for i in range(len(self.current_map)):
            for j in range(len(self.current_map[0])):
                if self.current_map[i][j] == "S":
                    self.current_map[i][j] = sign
                    return
                else:
                    continue

    def find_position(self, player_name):
        current_position = []
        to_find = self.players[player_name]['sign']
        for i in range(len(self.current_map)):
            for j in range(len(self.current_map[0])):
                if self.current_map[i][j] == to_find:
                    current_position.append(i)
                    current_position.append(j)
                    return current_position
                continue

    def move(self, player_name, direction):
        if player_name not in self.players:
            return "Go away sucker"
        pos = self.find_position(player_name)
        sign = self.players[player_name]['sign']
        if direction == "up":
            if self.can_move(pos[0]-1, pos[1], player_name):
                self.current_map[pos[0]][pos[1]] = "."
                self.current_map[pos[0]-1][pos[1]] = sign
                return True
            return False
        elif direction == "down":
            if self.can_move(pos[0]+1, pos[1], player_name):
                self.current_map[pos[0]][pos[1]] = "."
                self.current_map[pos[0]+1][pos[1]] = sign
                return True
            return False
        elif direction == "left":
            if self.can_move(pos[0], pos[1]-1, player_name):
                self.current_map[pos[0]][pos[1]] = "."
                self.current_map[pos[0]][pos[1]-1] = sign
                return True
            return False
        elif direction == "right":
            if self.can_move(pos[0], pos[1]+1, player_name):
                self.current_map[pos[0]][pos[1]] = "."
                self.current_map[pos[0]][pos[1]+1] = sign
                return True
            return False
        else:
            return False

    def can_move(self, x, y, player_name):
        if x >= 0 and \
           x < len(self.current_map) and \
           y >= 0 and \
           y < len(self.current_map[0]):
            if self.current_map[x][y] != "#" and self.current_map[x][y] == ".":
                return True
            elif self.current_map[x][y] != self.players[player_name]['sign']:
                print('Battle begins! Someone will DIE now')
                for player in self.players:
                    if self.players[player]['type'] == 'Hero':
                        hero = self.players[player]['class']
                    elif self.players[player]['type'] == 'Orc':
                        orc = self.players[player]['class']
                # print(players[0], players[1])
                Fight(hero, orc).simulate_fight()

            return False
        return False
