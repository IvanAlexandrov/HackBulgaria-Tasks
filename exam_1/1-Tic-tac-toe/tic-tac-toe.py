import machine
import player


class TicTacToe(object):

    def __init__(self):
        self.grid = [['.', '.', '.'],
                     ['.', '.', '.'],
                     ['.', '.', '.']]
        for i, grid in enumerate(self.grid):
            print('{}'.format(self.grid[i]))


game = TicTacToe()
player = player.Player()
machine = machine.Machine()
