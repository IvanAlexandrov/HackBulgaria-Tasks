class Machine(object):
    MACHINE_MOVES = 4
    SIGN = 'O'

    def __init__(self, name='Computer'):
        self.name = name
        self.moves = Machine.MACHINE_MOVES

    def change_name(self, name):
        self.name = name

    def make_research(self, grid):
        pass

    def make_decision(self, grid):
        pass

    def mark(self, grid, coords):
        self.moves -= 1
        if self.can_mark(grid, coords):
            grid[coords[0]][coords[1]] = Machine.SIGN

        return grid

    def can_mark(self, grid, coords):
        pass
