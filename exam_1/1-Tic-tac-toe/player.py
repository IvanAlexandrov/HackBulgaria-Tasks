class Player(object):
    PLAYER_MOVES = 5
    SIGN = 'X'

    def __init__(self, name='Player1'):
        self.name = name
        self.moves = Player.PLAYER_MOVES

    def change_name(self, name):
        self.name = name

    def mark(self, grid, coords):
        self.moves -= 1
        if self.can_mark(grid, coords):
            grid[coords[0]][coords[1]] = Player.SIGN

        return grid

    def can_mark(self, grid, coords):
        pass
